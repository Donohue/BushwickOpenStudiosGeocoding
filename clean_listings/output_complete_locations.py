#!/usr/bin/env python
import sys
import MySQLdb

'''
Update MySQL credentials

Prints unique location_id for given listings
Becomes input for ../detect_zones.py
'''

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(-1)

    f = open(sys.argv[1])
    con = MySQLdb.connect('<hostname>','<username>','<password>','<database>')
    cur = con.cursor()
    location_ids = []
    for line in f.readlines():
        parts = line.split(':')
        if len(parts) >= 3:
            location_id = parts[1].replace('"', '')
            address = parts[2].replace('"', '')
            if location_id != 'NULL':
                if not location_id in location_ids:
                    location_ids.append(location_id)
            else:
                found_location_id = None
                query = 'SELECT id FROM aib_location WHERE address LIKE "%s"' % address
                cur.execute(query)
                for row in cur:
                    found_location_id = row[0]
                    if not found_location_id in location_ids:
                        location_ids.append(found_location_id)
                if not found_location_id:
                    print 'Location ID not found'
    for location_id in location_ids:
        print location_id

if __name__ == '__main__':
    main()

