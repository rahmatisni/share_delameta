from conn_pg import connect_to_database
import json

# Call the function to establish the connection
conn = connect_to_database()
c = 'dbsharejmto'

data = {}
result = []

def getNullable(row, index1, index2, index3):
    try:
        print(row[index1][index2][index3])
        # print("exist")
        return row[index1][index2][index3]
    except Exception as e:
        # print("Index does not exist")
        return 'null'
# getNullable if connection is established
if conn is not None:
    try:
        # Perform database operations here
        # For example:
        cur = conn.cursor()
        # corrected SQL query
        cur.execute(
            f"SELECT * FROM {c}.tblshift_dinas_trne_ungaran_2023")
        rows = cur.fetchall()
        print(rows)

        for row in rows:
            # print(row)
            data['id'] = row[0]
            data['shift'] = row[0][0]
            data['tgl_lap'] = row[0][1:7]
            data['npp'] = row[0][7:13]
            data['lalin'] = {}
            # Initialize nested dictionaries for 'tunai', 'flo', 'e-toll', and 'dinas' under 'lalin'
            data['lalin']['tunai'] = {}
            data['lalin']['flo'] = {}
            data['lalin']['e-toll'] = {}
            data['lalin']['dinas'] = {}

            data['pendapatan'] = {}
            data['pendapatan']['tunai'] = {}
            data['pendapatan']['flo'] = {}
            data['pendapatan']['e-toll'] = {}
            data['pendapatan']['dinas'] = {}

            data['bank'] = {}
            data['bank']['lalin'] = {}
            data['bank']['pendapatan'] = {}

            data['bank']['lalin']['MDRI'] = {}
            data['bank']['lalin']['BRI'] = {}
            data['bank']['lalin']['BNI']= {}
            data['bank']['lalin']['BCA']= {}
            data['bank']['lalin']['DKI']= {}

            data['bank']['pendapatan']['MDRI'] = {}
            data['bank']['pendapatan']['BRI'] = {}
            data['bank']['pendapatan']['BNI']= {}
            data['bank']['pendapatan']['BCA']= {}
            data['bank']['pendapatan']['DKI']= {}

            # getNullable(row,1,0,1)           
            # Extract values for 'tunai' and 'flo' keys
            for i in range(6):
                data['lalin']['tunai']['golongan_'+str(i+1)] = getNullable(row,1,0,i)
                data['lalin']['flo']['golongan_'+str(i+1)] = getNullable(row,1,0,i)
                data['lalin']['e-toll']['golongan_'+str(i+1)] = getNullable(row,1,0,i)
                data['lalin']['dinas']['golongan_'+str(i+1)] = getNullable(row,1,0,i)
                data['pendapatan']['tunai']['golongan_' + str(i+1)] = getNullable(row,2,0,i)  
                data['pendapatan']['flo']['golongan_' + str(i+1)] = getNullable(row,2,1,i)  
                data['pendapatan']['e-toll']['golongan_' + str(i+1)] = getNullable(row,2,2,i)  
                data['pendapatan']['dinas']['golongan_' + str(i+1)] = getNullable(row,2,3,i)   
                data['bank']['lalin']['MDRI']['golongan_' + str(i+1)] = getNullable(row,3,0,i)  
                data['bank']['lalin']['BRI']['golongan_' + str(i+1)] = getNullable(row,3,1,i)  
                data['bank']['lalin']['BNI']['golongan_' + str(i+1)] = getNullable(row,3,2,i)  
                data['bank']['lalin']['BCA']['golongan_' + str(i+1)] = getNullable(row,3,3,i)  
                data['bank']['lalin']['DKI']['golongan_' + str(i+1)] = getNullable(row,3,4,i)  
                data['bank']['pendapatan']['MDRI']['golongan_' + str(i+1)] = getNullable(row,4,0,i) 
                data['bank']['pendapatan']['BRI']['golongan_' + str(i+1)] = getNullable(row,4,1,i)  
                data['bank']['pendapatan']['BNI']['golongan_' + str(i+1)] = getNullable(row,4,2,i)  
                data['bank']['pendapatan']['BCA']['golongan_' + str(i+1)] = getNullable(row,4,3,i)  
                data['bank']['pendapatan']['DKI']['golongan_' + str(i+1)] = getNullable(row,4,4,i)
      
            result.append(data)
    except Exception as e:
        print("Error karna ini:", e)
    finally:
        json_data = json.dumps(result, indent=4)

        print(json_data)

        conn.close()
        print("Connection closed.")
else:
    print("Connection not established. Exiting.")
