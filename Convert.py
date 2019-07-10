import json
import sys
from scipy.io import arff
import pandas as pd

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        print('test1')
        data = arff.loadarff('iris.arff')
        
        print('test2')
        for row in data:
            print(row)
        
        print('test3')



except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
