from conn_pg import connect_to_database
from conn_mysql import connect_to_database_mdb
import env


import json
from dotenv import load_dotenv
import os
load_dotenv()

def substring_after(s, delim):
    return s.partition(delim)[2]


def getDblistRT() :
    master = 'data_master'
    conn = connect_to_database_mdb(master)
    cur = conn.cursor()
    cur.execute("select * from tbl_gerbang where gerbang_nama NOT IN ('ALL', 'GB01', 'GB10') order by db asc")
    table_names = cur.fetchall()

    shareRTOrigin = []
    shareRTDest = []
    shareIDCabang = []

    for table in table_names:
        print(table)
        # if substring in table[0]:
        shareRTOrigin.append(table[2].lower().replace(" ", ""))
        shareRTDest.append(table[4])
        shareIDCabang.append(table[1])


    return (shareRTOrigin, shareRTDest, shareIDCabang)
