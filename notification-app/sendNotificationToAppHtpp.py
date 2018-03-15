import os
import json
import pyodbc

server = '//'
database = '//'
username = '//'
password = '//'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

try:
    postreqdata = json.loads(open(os.environ['req']).read())
except:
    postreqdata = open(os.environ['req']).read()

print(postreqdata)
Comment = postreqdata['comment']

sql = """SELECT TOP 1 AutoID  FROM Kwinana_Plc_notification 
        order by AutoId DESC"""

cursor.execute(sql)

ID = cursor.fetchone()[0]
print(ID)

sqlin = """UPDATE Kwinana_Plc_notification  set Comment = ? where  AutoId = ?"""
print(sqlin)

with cursor.execute(sqlin, Comment, ID):
    print("Record updated sucessfully")

response = open(os.environ['res'], 'w')
response.write("OK")
response.close()
