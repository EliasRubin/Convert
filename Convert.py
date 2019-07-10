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
            data = inFile.readlines()
            name,ext = os.path.splitext(inFile.name)
            
            dataSwitch = False
            header = ""
            newData = []
            for line in data:
                if not dataSwitch:
                    if "@attribute" in line:
                        attri = line.split()
                        column = attri[attri.index("@attribute")+1]
                        header = header + column + ","
                    elif "@data" in line:
                        dataSwitch = True
                        header = header[:-1]
                        header += '\n'
                        newData.append(header)            
                else:
                    newData.append(line)

            
            with open(name+".csv", "w") as outFile:
                outFile.writelines(newData)
            
        
         
       
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
            
            
            
         
