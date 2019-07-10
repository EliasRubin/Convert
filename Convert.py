import json
import sys

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        from scipy.io import arff
        import pandas as pd

        data = arff.loadarff('iris.arff')
        df = pd.DataFrame(data[0])

        df.head()




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
