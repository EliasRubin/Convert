import json
import sys
import arff
import numpy

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        data = arff.load(open('sys.argv[1]', 'rb'))
        
        for row in data:
            print(row)




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
