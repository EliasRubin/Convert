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

            
            for line in data:
                if not csvSwitch:
                    if "@attribute" in line:
                        attri = line.split()
                        column = attri[attri.index("@attribute")+1]
                        header = header + column + ","
                    elif "@data" in line:
                        csvSwitch = True
                        header = header[:-1]
                        newCsv.append(header)            
                else:
                    if line[0] == "%":
                        break
                    newCsv.append(line)

                    
            with open(name + ".csv", "w") as filecsv:
                filecsv.writelines(newCsv)
           
            
            

            
            headers = newCsv[0].split(",")
            i = 0
            while i < len(newCsv):
                newCsv[len(headers)-1] = newCsv[len(headers)-1][:-1]
                i += 1
            
            
            dataJson = []
            i = 0
            while i < len(headers):
                dataJson.append("")
                i += 1
            
            i = 1
            while i < len(newCsv):
                j = 0
                temp = newCsv[i].split(",")
                while j < len(headers):
                    dataJson[j] += temp[j]
                    dataJson[j] += ","
                    j += 1
                i += 1
            
            
            

            with open(name + ".json", 'w') as filejson: 
                i = 0
                while i < len(headers):
                    dataJson[i] = dataJson[i][:-1]
                    temp = dataJson[i].split(",")
                    #filejson.writelines(headers[i] + ': ' + temp)
                    filejson.writelines(temp)
                    i += 1
                
                
            
            
                
               

            
        
         
       
        




except FileNotFoundError:
            print('404 FILE NOT FOUND')
            exit(1)
            
            
            
         
