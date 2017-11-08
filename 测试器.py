#__author:"LIN SHIH-WAI"
#date:  2017/11/7
import urllib.request
# import csv
# f=open('C:\\data\\600000.csv','r+')
# read=csv.reader(f)
# for row in read:
#     print(row)

# import os
# import csv
#
# pathdir=os.listdir('C:\\data\\')
# print(pathdir)
#
# f=open('C:\\data\\600000.csv','r+')
# read_it=csv.reader(f)
# row=[row for row in read_it]
# print(row[0])
# print(type(row[0]))
# row[0].append('离差')
# print(row)

a=['a','b','c',1,2,3,4,2]
a2=['a','k','c',1]
a=set(a)
a2=set(a2)
print(list(a.intersection(a2)))
print(list(a2.intersection(a)))

for v,i in enumerate(a,1):
    if v==1:
        print(i)
        break
for i in a:
    print(i)
