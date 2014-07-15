#!/usr/bin/env python
import traceback
import sys

'''
Eliminates duplicate location_ids
Generally used as a sanity check before numbering
'''

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(-1)

    f = open(sys.argv[1])
    location_ids = []
    for line in f.readlines():
        location_id = int(line.replace('\n', ''))
        if not location_id in location_ids:
            location_ids.append(location_id)
            print location_id

if __name__ == '__main__':
    main()
