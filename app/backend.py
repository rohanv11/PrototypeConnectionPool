import mysql.connector
import os

def get_db_connection():
    db_config = {
        'host': os.environ.get('MYSQL_HOST'),
        'port': int(os.environ.get('MYSQL_PORT')),
        'user': os.environ.get('MYSQL_USER'),
        'password': os.environ.get('MYSQL_PASSWORD'),
        'database': os.environ.get('MYSQL_DATABASE')
    }
    try:
        cnx = mysql.connector.connect(**db_config)
        return cnx
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

def query_database(query):
    cnx = get_db_connection()
    if cnx:
        cursor = cnx.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            cnx.close()
            return results
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            cnx.rollback()
            cursor.close()
            cnx.close()
            return None
    return None

if __name__ == '__main__':
    # Example usage:
    data = query_database("SELECT 'Hello from MySQL!'")
    if data:
        print(f"Data from database: {data}")
    else:
        print("Failed to retrieve data.")