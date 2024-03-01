from datetime import datetime
from conn_pg import connect_to_database
from conn_mysql import connect_to_database_mdb
from getShareFromRuasRealTime import getDblistRT
# from tqdm import tqdm
import env


import json
from dotenv import load_dotenv
import os
load_dotenv()

# Call the function to establish the connection
# conn = connect_to_database()
c = os.getenv("schema_origin")
# c = env.schema_origin


listDB = getDblistRT()
listSource = listDB[0]
listDest = listDB[1]
idCabang = listDB[2]

# 0 source
# 1 dest

data = {}
result = []

def getNullable(row, index1, index2):
    try:
        res = int(row[index1][index2])
        # print("exist")
        # return row[index1][index2]
        return res
    except Exception as e:
        # print("Index does not exist")
        return 0

def insertData(data, indexA):
    # print(indexA)
    mdb_conn = connect_to_database_mdb(indexA)

    if mdb_conn.is_connected():
        try:
            cursor = mdb_conn.cursor()
            # print(data)
            sql = "INSERT INTO "+os.getenv("table_destination_realtime_share")+"(IdCabang,IdGerbang, Tanggal, Shift, Golongan, KodeInvestor, NamaInvestor, Tunai, RpeMandiri, RpeBri, RpeBni, RpeBca, RpeNobu, RpeDKI, RpeMega, RpDinasKary, RpDinasMitra, RpTotal, KodeIntegrator, json, flag, TanggalKirim, ResponseMessage, ResponseStatus, RpFlo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # sql = "INSERT INTO "+env.table_destination_realtime_share+"(IdCabang,IdGerbang, Tanggal, Shift, Golongan, KodeInvestor, NamaInvestor, Tunai, RpeMandiri, RpeBri, RpeBni, RpeBca, RpeNobu, RpeDKI, RpeMega, RpDinasKary, RpDinasMitra, RpTotal, KodeIntegrator, json, flag, TanggalKirim, ResponseMessage, ResponseStatus, RpFlo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            sql += " ON DUPLICATE KEY UPDATE Tunai = %s, RpeMandiri = %s, RpeBri = %s, RpeBni = %s, RpeBca = %s, RpeNobu = %s, RpeDKI = %s, RpeMega = %s, RpDinasKary = %s, RpDinasMitra = %s, RpTotal = %s, KodeIntegrator = %s, json = %s, flag = %s, TanggalKirim = %s, ResponseMessage = %s, ResponseStatus = %s, RpFlo = %s"
            cursor.execute(sql, data)
            mdb_conn.commit()
            # print("Data inserted successfully")
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            cursor.close()

def pairData(data, dest_table_name):
    dataqueryRes = []
    datas  = json.loads(data)

    for dataPendapatan in datas:
        jsData = dataPendapatan['Pendapatan']
        for key, value in jsData.items():
            total = 0
            dataSum = dataPendapatan['Pendapatan'][key]
            for values in dataSum.values():
                total += int(values)
            record = [dataPendapatan['IdCabang'], dataPendapatan['IdGerbang'],dataPendapatan['Tanggal'],dataPendapatan['Shift'],None,None,key,value['Tunai'],value['RpeMandiri'],value['RpeBri'],value['RpeBni'],value['RpeBca'],0,value['RpeDKI'],0,0,0,total,'DMB',None,None,None,None,None,value['RpeFlo']]
            onUpdate = [value['Tunai'],value['RpeMandiri'],value['RpeBri'],value['RpeBni'],value['RpeBca'],0,value['RpeDKI'],0,0,0,total,'DMB',None,None,None,None,None,value['RpeFlo']]
            record += onUpdate
            dataqueryRes.append(record.copy())

    mdb_conn = connect_to_database_mdb(dest_table_name)
    if mdb_conn:
        for indexA, dataToinsert in enumerate(dataqueryRes):
                    
        # for dataToinsert in dataqueryRes :
            try :
                insertData(dataToinsert, dest_table_name)
                if indexA % 60 == 0:
                    print(dest_table_name,indexA+1, '/', len(dataqueryRes), '=>', ((indexA+1) / len(dataqueryRes)) * 100, '%')
                elif indexA+1 == len(dataqueryRes) :
                    print(dest_table_name,indexA+1, '/', len(dataqueryRes), '=>', ('100%'))   
            except :
                print('Error')

    mdb_conn.close()

def executeShare() :
    for indexA, colsA in enumerate(listSource):
        print(colsA, '=>', listDest[indexA])
        Gerbangs = listDest[indexA][listDest[indexA].index("lattol_") + len("lattol_"):]
        Cabang = idCabang[indexA]

    # for connectionList in listSource :
        conn = connect_to_database()

        if conn is not None:
                # Perform database operations here
                # For example:
                cur = conn.cursor()
                origin_table_name = os.getenv("origin_table_name")
                dest_table_name = listDest[indexA]
                try :
                    # cur = conn.cursor()
                    cur.execute(
                        f"SELECT column_name FROM information_schema.columns WHERE table_schema = '{colsA}' AND table_name = '{origin_table_name}'")
                    columns = cur.fetchall()
                    column_names = [col[0] for col in columns]
                    cur.close()
                    cur = conn.cursor()
                    cur.execute(
                        f"SELECT TO_CHAR(to_date(SUBSTRING( id, 2, 6 ) , 'DDMMYY'),'YYYY-MM-DD') AS Tanggal, substr(id, 1,1) AS Shift, * FROM {colsA}.{origin_table_name}")
                    
                    rows = cur.fetchall()
                
                    for row in rows:
                        data['IdCabang'] = Cabang
                        data['Id'] = row[2]
                        data['Shift'] = row[1]
                        data['Tanggal'] = row[0]
                        data['IdGerbang'] = Gerbangs
                        data['Pendapatan'] = {}
                        for index, cols in enumerate(column_names):
                            if(cols != 'id' and cols != 'tanggal' and cols != 'shift'):
                                indexes = index+2
                                second_part = cols.split("_")[1]
                                inv = second_part.upper()
                                data['Pendapatan'][inv] = {
                                    'Tunai': getNullable(row, indexes, 0),
                                    'RpeMandiri': getNullable(row, indexes, 1),
                                    'RpeBri': getNullable(row, indexes, 2),
                                    'RpeBni': getNullable(row, indexes, 3),
                                    'RpeBca': getNullable(row, indexes, 4),
                                    'RpeFlo': getNullable(row, indexes, 5),
                                    'RpeDKI': getNullable(row, indexes, 6)
                                }
                        result.append(data.copy())
                    if len(result) > 0:
                        pairData(json.dumps(result), dest_table_name)
                    
                    

                    # with open(dest_table_name+".json", "w") as outfile:
                    #     outfile.write(json.dumps(result))
                    result.clear()
                # except Exception as e :
                #     print(e)
                except :
                    print('Source Tidak Ditemukan')
                    pass

                # finally:
                #     conn.close()
        else:
            print("Connection not established. Exiting.")
        conn.close()
