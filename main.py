import os

import M1 as m
import nmea_to_csv as c
import nema_to_kml_3 as kml

i=m.read_dir("C:\\nmea")
print (i)
for x in range (1,i+1):
    #c.create_csv(x)
    kml.create_kml(x)
