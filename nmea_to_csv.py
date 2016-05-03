import csv
import sqlite3
import M1 as m

#create_csv function - create the csv file
def create_csv(i,output,arr,filter):
    counter=0
    conn = sqlite3.connect('example.db')
    conn.text_factory = str
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM nmea"+str(i))
    name=output+'//'+'file'+str(i)+'.csv'
    with open("temp" , 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'latitude', 'north\south','longtitude','east\west','quality','nos','hdop','altitude','hog','speed','date'])
        for row in data:
            if (m.checkFilterLine(row,filter)==1):
                writer.writerow(row)
                counter=counter+1
    if not counter==0:
        with open("temp","rb") as source:
            rdr= csv.reader( source )
            with open(name,"wb") as result:
                wtr= csv.writer( result )
                for r in rdr:
                    #Checking the user preferences to filter
                    if (arr[10] == 0):
                        del r[11]
                    if (arr[9] == 0):
                        del r[10]
                    del r[9]
                    if (arr[8] == 0):
                        del r[8]
                    del r[7]
                    if (arr[6] == 0):
                        del r[6]
                    if (arr[5] == 0):
                        del r[5]
                    del r[4]
                    if (arr[3] == 0):
                        del r[3]
                    del r[2]
                    if (arr[1] == 0):
                        del r[1]
                    if (arr[0] == 0):
                        del r[0]
                    wtr.writerow(r)