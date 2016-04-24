#!/usr/bin/python

import sqlite3


def create_db():
    conn = sqlite3.connect('test.db')
    c=conn.cursor()
    c.execute(""""drop table if exists nmea""")

    conn.commit()
    c.execute('drop table if exists nmea')
    conn.execute('CREATE TABLE nmea'
                 '        (ID INT PRIMARY KEY     NOT NULL,\n'
                 '        time TEXT, latitude STRING,north STRING,\n'
                 '        longtitude STRING,east STRING,quality STRING, nos STRING,\n'
                 '        hdop STRING, altitude STRING, hog STRING)')
    print("Table created successfully")

    conn.close()



def add_to_db(str):
    list1=str.split(',')
    print (list1[1][1])
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO nmea VALUES (2, '2',?,'4','5','6','7','8','91','10','11')",[list1[1]])

    conn.commit()
    print("Records created successfully")
    conn.close()

create_db()
add_to_db("or,roni,ido")