#!/usr/bin/env python
import sys
import MySQLdb
import urllib
import urllib2
import json
import traceback

'''
Update MySQL credentials

Takes colon separated values
Finds all listings without location_id
Creates new location, and geocodes it
You should probably print the values and sanity check
before executing the query
'''

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(-1)

    f = open(sys.argv[1])
    con = MySQLdb.connect('<hostname>','<username>','<password>','<database>')
    cur = con.cursor()
    for line in f.readlines():
        parts = line.split(':')
        if len(parts) >= 3:
            location_id = parts[1].replace('"', '')
            address = parts[2].replace('"', '')
            if location_id != 'NULL':
                pass
            else:
                found_location_id = None
                query = 'SELECT id FROM aib_location WHERE address LIKE "%s"' % address
                cur.execute(query)
                for row in cur:
                    found_location_id = row[0]
                if not found_location_id:
                    proper_address = address + ', Brooklyn, NY'
                    params = urllib.urlencode({'address':proper_address,'sensor':'false'})
                    url = 'http://maps.googleapis.com/maps/api/geocode/json?' + params
                    try:
                        url_con = urllib2.urlopen(url)
                        result = json.loads(url_con.read())
                        if (len(result['results']) > 0):
                            zipcode = 'NULL'
                            for component in result['results'][0]['address_components']:
                                if 'postal_code' in component['types']:
                                    zipcode = component['long_name']
                            location = result['results'][0]['geometry']['location']
                            lat = location['lat']
                            lng = location['lng']
                            query = 'INSERT INTO aib_location (address,zip,lat,lng) VALUES ("%s","%s",%f,%f)' % (address, zipcode, lat, lng)
                            print query
                            #cur.execute(query)
                        else:
                            print 'No results for ' + address
                    except Exception, e:
                        print 'Error geocoding ' + address
                        traceback.print_exc()

if __name__ == '__main__':
    main()

