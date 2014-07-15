#!/usr/bin/env python

import MySQLdb
import sys
import traceback
import urllib
import urllib2
import json
import traceback

'''
Setup the MySQL hostname, username, password, database. Should be same for both connections.

Takes list of location_id
Geocodes each location
Updates the database
'''

try:
    f = open('./locations_to_geocode.csv')
    con = MySQLdb.connect('<hostname>','<username>','<password>','<database>')
    con2 = MySQLdb.connect('<hostname>','<username>','<password>','<database>')
    cur = con.cursor()
    cur2 = con2.cursor()
    for line in f.readlines():
        query = 'SELECT address FROM aib_location WHERE aib_location.id=' + str(int(line)) + ';'
        cur.execute(query)
        for row in cur:
            address = row[0] + ', Brooklyn, NY'
            params = urllib.urlencode({'address':address,'sensor':'false', 'key':'AIzaSyCYbE9ITCrsNyMRix8pwKJw5XxnyMxQ2ZM'})
            url = 'https://maps.googleapis.com/maps/api/geocode/json?' + params
            try:
                url_con = urllib2.urlopen(url)
                result = json.loads(url_con.read())
                if (len(result['results']) > 0):
                    location = result['results'][0]['geometry']['location']
                    lat = location['lat']
                    lng = location['lng']
                    query = 'UPDATE aib_location SET aib_location.lat=' + str(lat) + ', aib_location.lng=' + str(lng) + ' WHERE aib_location.id=' + str(int(line)) + ';'
                    cur2.execute(query)
                else:
                    print result
                    print 'No results for ID: ' + line
            except Exception, e:
                print 'Error geocoding for ID: ' + line
                traceback.print_exc()
except Exception, e:
    print 'Error'
    traceback.print_exc()
    sys.exit(-1)
finally:
    if con:
        con.close()
