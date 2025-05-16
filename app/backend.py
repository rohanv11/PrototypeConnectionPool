import asyncio
import aiomysql
import os
import time
import functools

def time_it(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f'function {func.__name__} time: {end_time - start_time}')
        return result
    return wrapper



# Get a single MySQL connection (no pooling)
@time_it
async def get_connection():
    return await aiomysql.connect(
        host=os.environ.get('MYSQL_HOST'),
        port=int(os.environ.get('MYSQL_PORT')),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PASSWORD'),
        db=os.environ.get('MYSQL_DATABASE'),
    )

# Run one sleep query on a new connection
async def run_sleep_query(i):
    conn = await get_connection()
    async with conn.cursor() as cur:
        await cur.execute("SELECT SLEEP(2);")
        print(f"Query {i} done")
    conn.close()

# Run N parallel queries
async def simulate_db_calls(n):
    start_time = time.time()
    print("Starting DB calls...")
    tasks = [run_sleep_query(i) for i in range(n)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print("Total time taken:", end_time - start_time)


connection_pool = None


class ConnectionPool():
    def __init__(self, size=10):
        self.size = size
        self.pool = asyncio.Queue(maxsize=size)

    async def create_connection_pool(self):
        for i in range(self.size):
            conn = await get_connection()
            await self.pool.put(conn)
    
    async def get_connection(self):
        return await asyncio.wait_for(self.pool.get(), timeout=20)

    async def close_connection(self, conn):
        await self.pool.put(conn)

    @time_it
    async def quit(self):
        for _ in range(self.size):
            conn = await self.pool.get()
            conn.close()
        
        print("Closed all connections in the pool")




# Run one sleep query on a new connection
async def run_sleep_query_use_pool(i, connection_pool: ConnectionPool, sem: asyncio.Semaphore):
    async with sem:
        conn = await connection_pool.get_connection()
        async with conn.cursor() as cur:
            await cur.execute("SELECT SLEEP(2);")
            print(f"Query {i} done")

        await connection_pool.close_connection(conn)



async def simulate_db_calls_using_connection_pool(n):
    start_time = time.time()
    pool_size = 10
    connection_pool = ConnectionPool(size=pool_size)
    sem = asyncio.Semaphore(pool_size)
    await connection_pool.create_connection_pool()
    end_time = time.time()
    print("Connection pool creation time", end_time - start_time)

    start_time = time.time()
    print("Starting DB calls...")
    tasks = [run_sleep_query_use_pool(i, connection_pool, sem) for i in range(n)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print("Total time taken using connectio pool:", end_time - start_time, "for", n, "calls")

    await connection_pool.quit()



if __name__ == '__main__':
    n = 1000
    # print(f"Simulating {n} parallel DB queries without pooling")
    # asyncio.run(simulate_db_calls(n))

    print(f"Simulating {n} parallel DB queries with CONNECTION POOL")
    asyncio.run(simulate_db_calls_using_connection_pool(n))

