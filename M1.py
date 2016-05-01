import os.path
import sqlite3
import datetime


# Create table
total=0
dates=[]
def read_dir(str):
    i=0
    global total
    if os.path.isdir(str):
       for file in os.listdir(str):
           if ".nmea" in file:
               i=i+1
               read_file(str+"\\"+file,i)
               total = i
    return i

def read_file(str1,i):
    with open (str1,'r')as f:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('drop table if exists nmea' + str(i))
        c.execute('CREATE TABLE IF NOT EXISTS summary(startDate text,endDate text,startTime text, endTime text,maxSpeed text,minSpeed text)')
        c.execute('''CREATE TABLE nmea''' + str(i) + '''
                (time text, latitude text,north text, longtitude text,
                east text,quality text, nos text, hdop text, altitude text,
                hog text,speed text,date text)''')
        list=f.readlines()
        index=0

        while index<len(list)-1:             # Go over all the lines in the current file
            index1 = find_GA(list,index)     # Finding the next GPGGA line
            if (index1==-1):                 # Checking if the GPGGA line is correct
                break
            line1 = checkLine(list[index1])  # Fix line
            index = index1+1
            index2 = findMC(list,index)      # Finding the next GPRMC line
            if (index2 == -1):               # Checking if the GPRMC line is correct
                break
            line2 = checkLine(list[index2])  # Fix line
            index=index2+1
            load_DB(line1,line2,i)           # Enter the lines into the database
       # startTime=c.execute('SELECT MIN(time) FROM summary')
       # print(startTime,"\n")
        conn.close()
    return 1


def checkLine(line):                         # checkLine Function - Fix the line to start with '$'
    if (line[0] != '$'):
        j = 0
        while line[j] != '$':
            j = j + 1
        line1 = line[j:]
        return line1
    return line
def find_GA(list,index):
    while "GPGGA" not in list[index] and index<len(list)-2:
        index=index+1
    if index >= len(list) - 1:
        return -1
    str=list[index].split(",")
    if (str[1]==''):
        return find_GA(list,index+1)

    return index
def findMC(list,index):
    while "GPRMC" not in list[index] and index<len(list)-2:
        index=index+1
    if index>=len(list)-1:
        return -1
    str=list[index].split(",")
    if (str[1]==''):
        return find_GA(list,index+1)
    return index
def load_DB(str1,str2,i):
    list1=str1.split(",")
    list2=str2.split(",")
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    # Insert a row of data
    c.execute("INSERT INTO nmea"+str(i)+" VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(list1[1], list1[2], list1[3], list1[4],list1[5], list1[6],list1[7], list1[8], list1[9], list1[10],list2[7],list2[9]))
    conn.commit()
    conn.close()

def checkFilterLine(line,filter):
        dateLine = datetime.date(int("20"+line[11][-2:]), int(line[11][2:4]), int(line[11][0:2]))
        #Checking date
        if not(filter[0]<=dateLine<=filter[1]):
            return 0
        #Checking start time
        if filter[0]==dateLine:
            timeLine = datetime.time(int(line[0][0:2]),int(line[0][2:4]),int(line[0][4:6]))
            if not timeLine>=filter[2]:
                return 0
        # Checking end time
        if filter[1] == dateLine:
            timeLine = datetime.time(int(line[0][0:2]), int(line[0][2:4]), int(line[0][4:6]))
            if not timeLine <= filter[3]:
                return 0
        #Checking altitude
        if not float(filter[4]) <= float(line[8])<=float(filter[5]):
                return 0
        #Checking speed
        if not float(filter[6])<=knots_to_kph(line[10])<= float(filter[7]):
            print "filter[6] = ",float(filter[6])
            print "line = ", knots_to_kph(line[10])
            print "filter[6] = ", float(filter[6])
            return 0
        #Checking NOS
        if not int(filter[8])<=int(line[6])<=int(filter[9]):
            return 0
        return 1

def knots_to_kph(value):
    return  (float(value) * 1.85200)

def dropAll():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    tables = list(c.execute("select name from sqlite_master where type is 'table'"))

    c.executescript(';'.join(["drop table if exists %s" % i for i in tables]))