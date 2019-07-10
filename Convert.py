import json
import sys
import os
from scipy.io import arff
import pandas as pd

if len(sys.argv) != 2:
    print('Error need the file')
    sys.exit(1)

try:
        
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            name,ext = os.path.splitext(file.name)
            
            csvSwitch = False
            header = ""
            newCsv = []
            newJson = {}
            newJson = []
            
            for line in data:
                if not csvSwitch:
                    if "@attribute" in line:
                        attri = line.split()
                        column = attri[attri.index("@attribute")+1]
                        header = header + column + ","
                    elif "@data" in line:
                        csvSwitch = True
                        header = header[:-1]
                        header += '\n'
                        newCsv.append(header)            
                else:
                    newCsv.append(line)

                    
           
            
            


            headers = newCsv[0].split(",")
            print(str(len(headers)))
            print(headers)
            
            i = 1
            while i < (len(newCsv)-1):
                j = 0
                temp = newCsv[i].split(",")
                print(str(len(temp)))
                item = '{ '
                while j < len(headers):
                    item += headers[j] + ': ' + temp[j] + ', '
                    j += 1
                item = item[:-2]
                item = item + ' }'
                newJson.append(item)
                i += 1
            
            
            
            
            with open(name + ".csv", "w") as filecsv:
                filecsv.writelines(newCsv)
                
               


            with open(name + ".json", 'w') as filejson:  
                json.dump(newJson, filejson)
            
        
         
       
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
            
            
            
         
