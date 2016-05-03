# nmea to kml class

import os.path
import sqlite3
import time
import M1 as m

#format_time function - return the time different format.
def format_time(value):
    hour = value[:2]
    minute = value[2:4]
    second = value[4:6]
    timeval = hour + ":" + minute + ":" + second
    return timeval

#format_date function - return the date different format
def format_date(value):
    day = value[:2]
    month = value[2:4]
    year = value[4:6]
    dateval = "20"+year+"-"+month+"-"+day
    return dateval

#knots_to_kph function - convert speed in knots to kmh
def knots_to_kph(value):
    return   str("%.2f" %(float(value)*1.85200)) +" km/h"

#create_kml function - create the kml file
def create_kml(i,output,arr,filter):
    my_category = 0
    skip=5
    database = sqlite3.connect('example.db')
    pois = database.execute("SELECT * FROM nmea" + str(i))
    file = output+'//'+'file' + str(i) + '.kml'
    FILE = open(file, 'w')
    FILE.truncate(0)
    FILE.write('<?xml version="1.0" encoding="iso-8859-1"?>\n')
    FILE.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    FILE.write('    <Document>\n')
    FILE.write('     <Folder>\n')
    FILE.write('     <name>Point Features</name>\n')
    FILE.write('     <description>Point Features</description>\n\n')
    j=0
    for poi in pois:
        if j%skip==0:
            if (m.checkFilterLine(poi,filter)==1):
                FILE.write('<Placemark>\n')
                FILE.write('    <TimeStamp>\n')
                FILE.write('     <when>%sT%s</when>\n' % (format_date(poi[11]),format_time(poi[0])))
                FILE.write('    </TimeStamp>\n')
                lat = float(poi[1][:2]) + (float(poi[1][2:]) / 60)
                lon = float(poi[3][:3]) + (float(poi[3][3:]) / 60)
                FILE.write('    <description><![CDATA[' )
                # Checking the user preferences to filter
                if(arr[10]==1):
                    FILE.write('Date: %s <br>' % format_date(poi[11]))
                if (arr[0] == 1):
                    FILE.write('Time: %s <br>' % format_time(poi[0]))
                if(arr[1]==1):
                    FILE.write('Latitude: %s %s <br>' % (str(lat),poi[4]))
                if(arr[3]==1):
                    FILE.write('Longtitude: %s %s <br>' % (str(lon),poi[2]))
                if (arr[8]==1):
                    FILE.write('Altitude: %s <br>' % poi[8])
                if (arr[9]==1):
                    FILE.write('Speed: %s <br>' % knots_to_kph(poi[10]))
                if(arr[5]==1):
                    FILE.write('Quality: %s <br>' % poi[5])
                if (arr[6] == 1):
                    FILE.write('Number of Satellites: %s <br>' % poi[6])
                FILE.write(']]></description>\n')
                FILE.write('    <Point>\n')

                FILE.write('        <coordinates>%sZ,%sZ,%s</coordinates>\n' % (str(lon), str(lat), poi[8]))
                FILE.write('    </Point>\n')
                FILE.write('</Placemark>\n')
                j=j+1
        else:
            j=j+1
    FILE.write('        </Folder>\n')
    FILE.write('    </Document>\n')
    FILE.write('</kml>\n')
    FILE.close()
    database.close()
