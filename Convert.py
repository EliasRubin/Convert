import json
import sys
from scipy.io import arff
import pandas as pd

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:

        data = arff.loadarff(sys.argv[1])
        df = pd.DataFrame(data[0])

        df.head()
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
