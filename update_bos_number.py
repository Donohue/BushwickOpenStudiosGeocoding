#!/usr/bin/env python
import traceback
import sys
import MySQLdb

'''
Setup MySQL credentials
Update MySQL column according to current year

Reads output of detect_zones.py
Updates the database with the appropriate number
'''

con = None
try:
    f = open(sys.argv[1])
    con = MySQLdb.connect('<hostname>','<username>','<password>','<database>')
    cur = con.cursor()
    for line in f.readlines():
        parts = line.split(',')
        location_id = int(parts[0])
        bos_number = parts[1]
        query = 'UPDATE aib_location SET aib_location.BOS14number="' + bos_number + '" WHERE aib_location.id=' + str(location_id)
        cur.execute(query)
except Exception, e:
    print 'Error occurred'
    traceback.print_exc()
    sys.exit(1)
finally:
    if con:
        con.close()

