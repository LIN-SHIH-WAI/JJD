#__author:"LIN SHIH-WAI"
#date:  2017/11/8
def E():
    return sum/count
import csv

# for i in range(60000,70000):
#     f=open('%s.csv','r+',newline='')%i
#     z=open('%sn.csv','w+',dialect='excel')
#     reader=csv.reader(f)
#     csv_write=csv.writer(z,dialect='excel')

f=open('600000.csv','r+')
z=open('600000n.csv','w+',newline='')#写入的时候必须关闭文件,否则报错
reader=csv.reader(f)
sum=0.0
count=-1
csv_write=csv.writer(z,dialect='excel')

for row in reader:
    list_now=[]
    if row[3] != '0.0':#去除没有价格的数据
        if row[0][0:4]=='2016':#只提取2016年的数据
            # count += 1
            # if count>=0:
            for i in range(0,15):
                list_now.append(row[i])
                # sum+=float(row[3])
            csv_write.writerow(list_now)
            print(reader.line_num,row)
print(row[0])
print(row[0][0:4])
