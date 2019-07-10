#!/usr/bin/env python3
import csv

with open(sys.argv[1]) as csvf:
    cr = csv.reader(csvf, delimiter = ',')
    for row in cr:
        print(row)
