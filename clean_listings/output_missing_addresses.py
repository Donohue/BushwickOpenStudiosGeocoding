#!/usr/bin/env python
import sys
import re

_digits = re.compile('\d')
def contains_digits(d):
    return bool(_digits.search(d))

'''
Takes colon separated file
Outputs same file with incomplete addresses
'''

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <filename>' % sys.argv[0]
        sys.exit(-1)

    f = open(sys.argv[1])
    for line in f.readlines():
        parts = line.split(':')
        location_id = parts[1].replace('"', '')
        address = parts[2].replace('"', '')
        if location_id != 'NULL':
            pass
        elif not contains_digits(address):
            print ':'.join([str(x).replace('\n', '') for x in parts])
if __name__ == '__main__':
    main()

