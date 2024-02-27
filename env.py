import os

version = "DWH VERSION 1.0.0-AT4-2023"

intervalQuery = 1

############## MIY PCDS ################
# 4 20 = src - Mariddb Versi 5 PCDS OPEN/EXIT (MIY)
#21 = src - Mariadb Versi 5 PCDS ENTRANCE (MIY)
#23 = src - Mariadb Versi 5 PCDS ENTRANCE & EXIT (MIY)

# 5 30 = src - Mariadb Versi 10 PCDS OPEN/EXIT (MIY)
#31 = src - Mariadb Versi 10 PCDS ENTRANCE (MIY)
#33 = src - Mariadb Versi 10 PCDS ENTRANCE & EXIT (MIY)

############### MIY BCDS ###################
# 7 40 = src - Mariadb Versi 5 BCDS OPEN/EXIT (MIY)

# 8 50 = src - Mariadb Versi 10 BCDS OPEN/EXIT (MIY)

############### DELAMETA ###################
# 6 60 = Delameta - PostgreSQL OPEN (DELAMETA)
# 10 61 = Delameta - PostgreSQL CLOSE ENTRANCE (DELAMETA)
# 11 62 = Delameta - PostgreSQL CLOSE EXIT (DELAMETA)
# 9 63 = Delameta - PostgreSQL CLOSE ENTRANCE & EXIT (DELAMETA)
############### JMTO #######################
# 99 = JMTO


# configMode=os.environ['CFG_MODE']
# jmtoHost=os.environ['IP_MEDIASI']
# jmtoUser=os.environ['USER_MEDIASI']
# jmtoPass=os.environ['PASS_MEDIASI']
# jmtoDb= os.environ['DB_MEDIASI']
# jmtoPort= os.environ['DB_PORT']

# idGerbang= os.environ['GERBANG_SRC']
# namaGerbang= os.environ['GERBANG_NAMA']
# srcHost=os.environ['IP_SRC']
# srcUser=os.environ['USER_SRC']
# srcPass=os.environ['PASS_SRC']
# srcDb=os.environ['DB_SRC']
# srcPort=os.environ['PORT_SRC']

configMode='60'
idGerbang='37'
namaGerbang='nusadua'

# Server Mediasi JMTO
jmtoHost='179.10.110.252'
jmtoUser='mediasi'
jmtoPass='@jap3k'
jmtoDb='japek_lattol_37'
jmtoPort='3306' 

# # # # Source
# srcHost="10.14.37.8"
# srcUser="jmTo"
# srcPass="jmTo@2023!"
# srcDb="warehouse_jmto"
# srcPort="3306"


srcHost="127.0.0.1"
srcUser="postgres"
srcPass="password"
srcDb="bali"
srcPort="5432"

# Server Mediasi JMTO
# jmtoHost='172.181.90.2'
# jmtoUser='jangermediasi'
# jmtoPass='@KTB2MMS'
# jmtoDb='cikupa_lattol'
# jmtoPort='3306' 


# driverSQL="{ODBC Driver 17 for SQL Server};"
# srcHost="192.168.41.25;"
# srcUser="jm;"
# srcPass="1ntegr@s1;"
# srcDb="master;"
# srcPort="1433;"

host_origin = '172.20.15.253'
user_origin = 'jmto'
pwd_origin = 'jmt02023!#'
table_origin = 'tblatt4_bagihasil_'
schema_origin = 'dbsharejmto'

host_destination = '179.10.120.252'
user_destination = 'mediasi'
pwd_destination = '@jpm'
table_destination = 'jid_rekap_pendapatan_2023'
table_destination_realtime_share = 'jid_rekap_pendapatan_db'

ruas = 'JPM'
gerbang_id = '22'


