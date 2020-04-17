import mysql.connector
from mysql.connector import Error

HOST = 'localhost'
DATABASE_NAME = 'college_software'
USERNAME = 'root'
PASSWORD = ''

connection = mysql.connector.Connect(host=HOST, user=USERNAME, password=PASSWORD)

cursor = connection.cursor()
cursor.execute('use information_schema;')
cursor.execute('SELECT COUNT(*) FROM schemata WHERE SCHEMA_NAME="'+DATABASE_NAME+'";')
if cursor.fetchone()[0] == 0:
    print("New Database")
else:
    print("Database Exists")

connection.close()
