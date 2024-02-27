import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

def connect_to_database():
    dbname = os.getenv("ruas")
    user = os.getenv("user_origin")
    password = os.getenv("pwd_origin")
    host = os.getenv('host_origin')
    port = '5432'  # or your port number

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection established successfully!")
        return conn

    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)
        return None
