from conn_pg import connect_to_database
from conn_mysql import connect_to_database_mdb


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
    # Execute the SQL query
    cur.execute("select * from tbl_gerbang where gerbang_nama <> 'ALL' order by db asc")
                
    # Fetch all the results
    table_names = cur.fetchall()
    # print(table_names)
    # substring = "bagihasil"

    shareRTOrigin = []
    shareRTDest = []
    shareIDCabang = []

    # # 
    # # Print the table names
    for table in table_names:
        print(table)
        # if substring in table[0]:
        shareRTOrigin.append(table[2].lower().replace(" ", ""))
        shareRTDest.append(table[5])
        shareIDCabang.append(table[1])


    return (shareRTOrigin, shareRTDest, shareIDCabang)
        
    # # print(table_share_origin, table_share_destination)
    # # Close the cursor and connection
    # cur.close()
    # conn.close()
    # return (table_share_origin, table_share_destination)
