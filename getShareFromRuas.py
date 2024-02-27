from conn_pg import connect_to_database
import json
from dotenv import load_dotenv
import os

load_dotenv()

def substring_after(s, delim):
    return s.partition(delim)[2]


def getDblist() :
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("select * from (SELECT table_name FROM information_schema.tables WHERE table_schema = 'dbsharejmto' AND table_type = 'BASE TABLE') as nama_tabel where table_name like '%bagihasil%' order by table_name asc")
                
    table_names = cur.fetchall()
    substring = "bagihasil"

    table_share_origin = []
    table_share_destination = []

    for table in table_names:
        if substring in table[0]:
            table_share_origin.append(table[0])
            x = substring_after(table[0], "bagihasil_")
            table_share_destination.append(x)
            
    cur.close()
    conn.close()
    return (table_share_origin, table_share_destination)