from conn_pg import connect_to_database

import json
from dotenv import load_dotenv
import os
load_dotenv()

def getDblist() :
    conn = connect_to_database()
    cur = conn.cursor()
    # Execute the SQL query
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'dbsharejmto'
            AND table_type = 'BASE TABLE';
    """)
                
    # Fetch all the results
    table_names = cur.fetchall()
    substring = "bagihasil"

    table_share_origin = []
    table_share_destination = []

    # 
    # Print the table names
    for table in table_names:
        if substring in table[0]:
            table_share_origin.append(table[0])
            index = table[0].find('bagihasil')
            if index != -1:
                substring = table[0][index + len('bagihasil') + 1:]
                table_share_destination.append(substring)
        
    # print(table_share_origin, table_share_destination)
    # Close the cursor and connection
    cur.close()
    conn.close()

    return (table_share_origin, table_share_destination)