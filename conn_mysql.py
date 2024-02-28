import mysql.connector
from dotenv import load_dotenv
import os
import env

load_dotenv()

def connect_to_database_mdb(databaseName):
    # print(databaseName, '1')
    try:
        connection = mysql.connector.connect(
            host= os.getenv("host_destination"),
            user= os.getenv("user_destination"),
            password= os.getenv("pwd_destination"),
            database= databaseName

            # host= env.host_destination,
            # user= env.user_destination,
            # password= env.pwd_destination,
            # database= databaseName
        )
        if connection.is_connected():
            i = 1
            # print('Connected to MariaDB database')
        return connection

    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None

