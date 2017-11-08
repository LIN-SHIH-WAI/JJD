#__author:"LIN SHIH-WAI"
#date:  2017/11/8
#--------------------------模块区域------------------------------------
import csv
import os
#--------------------------函数定义区域--------------------------------
#目录下文件列表函数 用于for循环
def readfilename(path):#形成目录下的所有文件名.
    return os.listdir(path)
#--------------------------初始筛选-------------------------------
while True:
    first_does=input('请输入是否要筛选原始数据y/n:')

    if first_does=='n':
        break
    if first_does=='y':
        print('在执行的时候必须关闭原始的csv文件否则无法工作')
        pathdir=readfilename('C:\\data\\')
        for i in pathdir:
            print('正在提取:',i)
            f=open('C:\\data\\%s'%i,'r+')
            z=open('C:\\测试提取\\%s'%i,'w+',newline='')
            reader=csv.reader(f)
            csv_write=csv.writer(z,dialect='excel')
            for row in reader:
                list_now = []
                if row[3] != '0.0':  # 去除没有价格的数据
                    if row[0][0:4] == '2016':  # 只提取2016年的数据
                        for i in range(0, 15):
                            list_now.append(row[i])
                        csv_write.writerow(list_now)
    else:
        continue
#------------------------对筛选后的数据进行处理------------------
#1.求出期望收益率
#2.算出他们的方差(得到一年的期望收益率和方差)
#3.计算协方差
pathdir=readfilename('C:\\测试提取\\')
for i in pathdir:
    print('正在处理:',i)
    f=open('C:\\测试提取\\%s'%i,'r+')
    read_it=csv.reader(f)
    for row in read_it:
        print(row)
