#__author:"LIN SHIH-WAI"
#date:  2017/11/7
import urllib.request
# import csv
# f=open('C:\\data\\600000.csv','r+')
# read=csv.reader(f)
# for row in read:
#     print(row)

import os
import csv

pathdir=os.listdir('C:\\data\\')
print(pathdir)

f=open('C:\\data\\600000.csv','r+')
read_it=csv.reader(f)
row=[row for row in read_it]
print(row[0])
print(type(row[0]))
row[0].append('离差')
print(row)