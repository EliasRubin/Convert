import json
import sys
import os
from scipy.io import arff
import pandas as pd

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        
        with open(sys.argv[1], "r") as inFile:
            content = inFile.readlines()
            name,ext = os.path.splitext(inFile.name)
            
            data = False
            header = ""
            newContent = []
            for line in content:
                if not data:
                    if "@attribute" in line:
                        attri = line.split()
                        columnName = attri[attri.index("@attribute")+1]
                        header = header + columnName + ","
                    elif "@data" in line:
                        data = True
                        header = header[:-1]
                        header += '\n'
                        newContent.append(header)
                    else:
                        newContent.append(line)
                        new = newContent

            with open(name+".csv", "w") as outFile:
            outFile.writelines(new)
        
         
       
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
            
            
            
         
