Implement a simple connection pool using Bounded Blocking Queue.

docker-compose up -d    
docker-compose up --build -d

if i want to take backup for a volume:
docker run -it --rm -v db_data:/data alpine:latest sh -c "ls -l /data"

Using a Utility Container: You can run a temporary container with the same volume mounted to access the files directly from within that container's shell. For example:

This command will run an Alpine Linux container, mount your db_data volume to /data inside the container, and list the contents. You can then use other commands like cp or tar within the container to move or archive the data.



MYSQL users query:
SELECT User, Host FROM mysql.user;


PRIVILIEGES sql

DROP USER IF EXISTS 'rohan@123'@'%';

CREATE USER 'rohan123'@'%' IDENTIFIED BY 'rohan123';
GRANT ALL PRIVILEGES ON dummy_db.* TO 'rohan123'@'%';
FLUSH PRIVILEGES;


docker-compose down -v  # stops and deletes containers AND volumes
docker-compose up --build

DOCKER:
| Action                       | Command                                          |
| ---------------------------- | ------------------------------------------------ |
| Start only app               | `docker-compose up python-app`                   |
| Stop only app                | `docker-compose stop python-app`                 |
| Rebuild only app             | `docker-compose up --build python-app`           |
| Rebuild app w/o affecting DB | `docker-compose up --build --no-deps python-app` |
| Check container status       | `docker ps -a`                                   |


for n = 10 and n = 50 and n = 100
 Total time taken: 7.059006214141846


n = 50
Simulating 50 parallel DB queries without pooling
python-app  | Starting DB calls...
python-app  | function get_connection time: 0.0074787139892578125
python-app  | function get_connection time: 0.00635218620300293
python-app  | function get_connection time: 0.005217790603637695
python-app  | function get_connection time: 0.00688934326171875
python-app  | function get_connection time: 0.004159212112426758
python-app  | function get_connection time: 0.004046440124511719
python-app  | function get_connection time: 0.003765583038330078
python-app  | Query 0 done
python-app  | Query 3 done
python-app  | Query 6 done
python-app  | Query 1 done
python-app  | Query 16 done
python-app  | Query 17 done
python-app  | Query 20 done
python-app  | function get_connection time: 5.036950349807739
python-app  | function get_connection time: 5.035995721817017
python-app  | function get_connection time: 5.03706431388855
python-app  | function get_connection time: 5.038022041320801
python-app  | function get_connection time: 5.0373687744140625
python-app  | function get_connection time: 5.037784099578857
python-app  | function get_connection time: 5.03713846206665
python-app  | function get_connection time: 5.036206245422363
python-app  | function get_connection time: 5.039611577987671
python-app  | function get_connection time: 5.0385565757751465
python-app  | function get_connection time: 5.037527799606323
python-app  | function get_connection time: 5.037322759628296
python-app  | function get_connection time: 5.036961555480957
python-app  | function get_connection time: 5.036456346511841
python-app  | function get_connection time: 5.038229703903198
python-app  | function get_connection time: 5.0364930629730225
python-app  | function get_connection time: 5.036518096923828
python-app  | function get_connection time: 5.036471366882324
python-app  | function get_connection time: 5.0372209548950195
python-app  | function get_connection time: 5.0367043018341064
python-app  | function get_connection time: 5.036851406097412
python-app  | function get_connection time: 5.03838038444519
python-app  | function get_connection time: 5.0371315479278564
python-app  | function get_connection time: 5.036819219589233
python-app  | function get_connection time: 5.037020206451416
python-app  | function get_connection time: 5.037043333053589
python-app  | function get_connection time: 5.036894083023071
python-app  | function get_connection time: 5.03709077835083
python-app  | function get_connection time: 5.037640333175659
python-app  | function get_connection time: 5.037121534347534
python-app  | function get_connection time: 5.037616014480591
python-app  | function get_connection time: 5.0370354652404785
python-app  | function get_connection time: 5.037289619445801
python-app  | function get_connection time: 5.037794828414917
python-app  | function get_connection time: 5.0374979972839355
python-app  | function get_connection time: 5.037226438522339
python-app  | function get_connection time: 5.037759304046631
python-app  | function get_connection time: 5.03778600692749
python-app  | function get_connection time: 5.037584543228149
python-app  | function get_connection time: 5.03750205039978
python-app  | function get_connection time: 5.037858724594116
python-app  | function get_connection time: 5.038295269012451
python-app  | function get_connection time: 5.037726879119873
python-app  | Query 11 done
python-app  | Query 26 done
python-app  | Query 32 done
python-app  | Query 44 done
python-app  | Query 37 done
python-app  | Query 45 done
python-app  | Query 39 done
python-app  | Query 9 done
python-app  | Query 19 done
python-app  | Query 46 done
python-app  | Query 5 done
python-app  | Query 28 done
python-app  | Query 25 done
python-app  | Query 21 done
python-app  | Query 15 done
python-app  | Query 14 done
python-app  | Query 7 done
python-app  | Query 18 done
python-app  | Query 4 done
python-app  | Query 10 done
python-app  | Query 22 done
python-app  | Query 27 done
python-app  | Query 38 done
python-app  | Query 2 done
python-app  | Query 12 done
python-app  | Query 23 done
python-app  | Query 13 done
python-app  | Query 43 done
python-app  | Query 40 done
python-app  | Query 42 done
python-app  | Query 48 done
python-app  | Query 41 done
python-app  | Query 36 done
python-app  | Query 35 done
python-app  | Query 34 done
python-app  | Query 24 done
python-app  | Query 49 done
python-app  | Query 29 done
python-app  | Query 47 done
python-app  | Query 31 done
python-app  | Query 8 done
python-app  | Query 30 done
python-app  | Query 33 done
python-app  | Total time taken: 7.059697866439819


n = 100
Total time taken: 7.074038028717041

n = 150 
Total time taken: 7.100616931915283

n = 200
pymysql.err.OperationalError: (1040, 'Too many connections')





WITH CONNECTION POOL:


n = 10

python-app  | Simulating 10 parallel DB queries with CONNECTION POOL
python-app  | function get_connection time: 5.015982389450073
python-app  | function get_connection time: 0.0032927989959716797
python-app  | function get_connection time: 0.002641439437866211
python-app  | function get_connection time: 0.0019855499267578125
python-app  | function get_connection time: 0.0021505355834960938
python-app  | function get_connection time: 0.002293109893798828
python-app  | function get_connection time: 0.0016682147979736328
python-app  | function get_connection time: 0.0015914440155029297
python-app  | function get_connection time: 0.0018308162689208984
python-app  | function get_connection time: 0.005715608596801758
python-app  | Connection pool creation time 5.039489269256592
python-app  | Starting DB calls...
python-app  | Query 2 done
python-app  | Query 6 done
python-app  | Query 1 done
python-app  | Query 3 done
python-app  | Query 9 done
python-app  | Query 0 done
python-app  | Query 5 done
python-app  | Query 8 done
python-app  | Query 7 done
python-app  | Query 4 done
python-app  | Total time taken using connectio pool: 2.013690233230591 for 10 calls


for n = 50 (needed to increase the timeout from 5 to 10 secs, for getting connection, else was 
gettting timeout error)

python-app  | Simulating 50 parallel DB queries with CONNECTION POOL
python-app  | function get_connection time: 0.0032312870025634766
python-app  | function get_connection time: 0.0006132125854492188
python-app  | function get_connection time: 5.01468300819397
python-app  | function get_connection time: 0.0038912296295166016
python-app  | function get_connection time: 0.0025091171264648438
python-app  | function get_connection time: 0.002123594284057617
python-app  | function get_connection time: 0.002198934555053711
python-app  | function get_connection time: 0.001796722412109375
python-app  | function get_connection time: 0.0018222332000732422
python-app  | function get_connection time: 0.0017154216766357422
python-app  | Connection pool creation time 5.034846067428589
python-app  | Starting DB calls...
python-app  | Query 2 done
python-app  | Query 1 done
python-app  | Query 3 done
python-app  | Query 0 done
python-app  | Query 4 done
python-app  | Query 5 done
python-app  | Query 6 done
python-app  | Query 7 done
python-app  | Query 8 done
python-app  | Query 9 done
python-app  | Query 10 done
python-app  | Query 11 done
python-app  | Query 16 done
python-app  | Query 15 done
python-app  | Query 19 done
python-app  | Query 13 done
python-app  | Query 18 done
python-app  | Query 12 done
python-app  | Query 17 done
python-app  | Query 14 done
python-app  | Query 21 done
python-app  | Query 20 done
python-app  | Query 22 done
python-app  | Query 23 done
python-app  | Query 24 done
python-app  | Query 25 done
python-app  | Query 26 done
python-app  | Query 27 done
python-app  | Query 28 done
python-app  | Query 29 done
python-app  | Query 30 done
python-app  | Query 31 done
python-app  | Query 32 done
python-app  | Query 33 done
python-app  | Query 36 done
python-app  | Query 35 done
python-app  | Query 34 done
python-app  | Query 37 done
python-app  | Query 38 done
python-app  | Query 39 done
python-app  | Query 40 done
python-app  | Query 41 done
python-app  | Query 47 done
python-app  | Query 42 done
python-app  | Query 44 done
python-app  | Query 46 done
python-app  | Query 45 done
python-app  | Query 49 done
python-app  | Query 43 done
python-app  | Query 48 done
python-app  | Total time taken using connectio pool: 10.034509658813477 for 50 calls


n = 100 (increasing wait for timeout 10 to 15) still no
(increasing wait for timeout 15 to 20) ...Worked

Total time taken using connection pool: 20.05656933784485 for 100 calls



n = 150 (increasing wait for timeout 20 to 25) still no
(increasing wait for timeout 25 to 30) ...worked

Total time taken using connectio pool: 30.084621906280518 for 150 calls


n = 200
(increasing wait for timeout 30 to 40) ...worked

Total time taken using connectio pool: 40.156426668167114 for 200 calls


Here the problem is, since i am running 200 queries at the same time, 
but pool has max of 10 connections.

so ideal max time would be = ( 200 / 10 ) * per_batch_time
                           = ( 200 / 10 ) * 2
                           = 40 secs

100 queries → (100/10) * 2 = 20 seconds
And thus, some queries are doing a get_connection and waiting for around 40 secs max.

Solution:
Increase the timeout.
Use a semaphore or task queue instead of trying to run all n tasks in parallel.
In asyncio, a semaphore works exactly the same way for limiting concurrent coroutines.

This creates a semaphore that allows up to 10 concurrent coroutines to enter a critical section (a block of code that should only be run by a limited number of tasks).


with semaphore implementation, timeout constant as 20 secs for below n calls.

n = 200
Total time taken using connectio pool: 40.144052267074585 for 200 calls

n = 500
Total time taken using connectio pool: 100.31867837905884 for 500 calls.

n = 1000
Total time taken using connectio pool: 200.67818117141724 for 1000 calls.


Drawback/advantage.
Only 10 tasks are asking for a connection at once, rest are in queue.
