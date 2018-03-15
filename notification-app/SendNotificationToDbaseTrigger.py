from datetime import datetime
import json
import os
import pyodbc

server = '///'
database = '///'
username = '///'
password = '///'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

dt = datetime.now()
dd = datetime.date(dt)

curs = cnxn.cursor()

df = ''
try:
    postreqdata = json.loads(open(os.environ['req']).read())
    df = postreqdata[0]
except:
    postreqdata = open(os.environ['req']).read()
    df = postreqdata[0]




conveyor, dest, par = ('', '', ()) 

validate = """SELECT TOP 1 Commodity, TrainId, Notifyday, Comment 
                 FROM Kwinana_Plc_notification where Commodity = ? 
                 and TrainId = ? and Notifyday = ? order by AutoId DESC"""

insert = """INSERT INTO Kwinana_Plc_notification
           (ConveyorBelt, Commodity, Grade, TPH_Setpoint, Destination, 
           TrainId, Notifyday) VALUES (?,?,?,?,?,?,?)"""

retvar = ''
print(df['destination'])

try:
    conveyor = df['tphsetpoint'].split(":")[0]
    tphsetpoint = df['tphsetpoint'].split(":")[1]
    par = (conveyor, df['commodity'], df['grade'], tphsetpoint, df['destination'], df['trainid'], dd)
    print('par', par)

    #check if there is already an entry
    curs.execute(validate, df['commodity'], str(df['trainid']), dd) 
    row = curs.fetchall()
    print(row)
    if row == []:
        with curs.execute(insert, par):
            print("Record inserted sucessfully")
    else:
        print("Record already Exists")
except Exception as e:
    retvar = str(e)
    print(retvar)
else:
    retvar = "OK"

response = open(os.environ['res'], 'w')
response.write(retvar)
response.close()