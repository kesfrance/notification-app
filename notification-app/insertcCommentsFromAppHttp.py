from datetime import datetime
from datetime import timedelta
import os
import json
import pyodbc
from azure.storage.blob import AppendBlobService

mykey = "///"
myaccount = "//"

server = '///'
database = '///'
username = '///'
password = '///'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()


sql = """SELECT TOP 1 t1.Comment, t1.Commodity, t1.TPH_Setpoint, 
      t2.Tph_RecSetpoint, t1.ConveyorBelt, t1.Destination  
      FROM Kwinana_Plc_notification t1 join Kwinana_Plc_refference_data
      t2 on t1.Commodity = t2.Commodity order by AutoId DESC"""

def wa_timenow(): 
    #get current perth time
    dtn = datetime.now() + timedelta(hours=8)
    return dtn

cursor.execute(sql)
row = cursor.fetchone()
outval = ''
if row[0] == None:
    outval = ",".join([str(i) for i in row[1:]])
    
    #connect to request-log blob and log request
    append_blob_service = AppendBlobService(account_name=myaccount, account_key=mykey)
    append_blob_service.append_blob_from_text('requestlogs', 
                                'request.txt',"%s,%s "% (wa_timenow(), outval))
    append_blob_service.append_blob_from_text('requestlogs', 
                                'request.txt',"\n")
    append_blob = append_blob_service.get_blob_to_text('requestlogs', 'request.txt')


#send response
response = open(os.environ['res'], 'w')

response.write(outval)
response.close()