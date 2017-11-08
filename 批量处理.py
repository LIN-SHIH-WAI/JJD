#__author:"LIN SHIH-WAI"
#date:  2017/11/8
def E():
    return sum/count
import csv

# for i in range(60000,70000):
#     f=open('%s','r+',encoding='utf-8')%i
#     reader=csv.reader(f)
#


f=open('600000.csv','r+')
z=open('600000n.csv','w+',newline='')
reader=csv.reader(f)
sum=0.0
count=-1
csv_write=csv.writer(z,dialect='excel')

for row in reader:
    list_now=[]
    if row[3] != '0.0':
        count += 1
        if count>=0:
            for i in range(0,15):
                list_now.append(row[i])
                # sum+=float(row[3])
            csv_write.writerow(list_now)
            print(reader.line_num,row)
print(row[0])
print(type(row[0][0:4]))
