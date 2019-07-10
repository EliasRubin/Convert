#!/usr/bin/env python3
import csv
import sys
import argparse


with open('sys.argv[1]', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
