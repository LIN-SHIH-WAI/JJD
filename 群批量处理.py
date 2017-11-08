#__author:"LIN SHIH-WAI"
#date:  2017/11/8
#--------------------------模块区域------------------------------------
import csv
import os

import os.path
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
        break
    else:
        continue
#-----------------------删除退市的股票信息-----------------
pathdir=readfilename('C:\\测试提取\\')
for i in pathdir:
    filesize = os.path.getsize('C:\\测试提取\\%s'%i)/1024/1024
    if float(filesize)==0.0:
        os.remove('C:\\测试提取\\%s'%i)
        print('删除退市信息',i)

#------------------------对筛选后的数据进行处理------------------
#1.求出期望收益率
#2.算出他们的方差(得到一年的期望收益率和方差)
#3.计算协方差
#4.计算β #指数用上证指数.


#1.求出期望收益

dict_information={}#记录每个文件的期望,方差.
pathdir=readfilename('C:\\测试提取\\')
for i in pathdir:#读取每个特定的
    sum_it=0.0
    f=open('C:\\测试提取\\%s'%i,'r+')
    read_it=csv.reader(f)
    dict_information.setdefault('%s'%i,{})
    dict_information['%s'%i].setdefault('期望',0.0)
    dict_information['%s'%i].setdefault('方差',0.0)
    dict_information['%s'%i].setdefault('数据数量',0)
    dict_information['%s'%i].setdefault('加总',0)
    dict_information['%s'%i].setdefault('协方差',{})
    for count,row in enumerate(read_it,1):
        sum_it+=float(row[3])
    dict_information['%s'%i]['期望']=sum_it/count
    dict_information['%s'%i]['数据数量']=count
    dict_information['%s'%i]['加总']=sum_it
print(dict_information)

#2求出方差
for i in pathdir:#读取每个特定的
    方差=0
    离差=0
    离差平方和=0
    print('正在处理:',i)
    f=open('C:\\测试提取\\%s'%i,'r+')
    read_it=csv.reader(f)
    for row in read_it:
        离差=float(row[3])-dict_information[i]['期望']
        离差平方=离差*离差
        离差平方和+=离差平方
        if dict_information[i]['数据数量']==1:
            方差=离差平方和/(dict_information[i]['数据数量'])
        else:
            方差 = 离差平方和 / (dict_information[i]['数据数量']-1)#如果样本数>1 要-1
        dict_information['%s' % i]['方差'] = 方差
print(dict_information)
#计算协方差
pathdir=readfilename('C:\\测试提取\\')
zz=open('记录.txt','w+',encoding='utf-8')
for i in pathdir:#读取每个文件 #第一个文件
    f=open('C:\\测试提取\\%s'%i,'r+')
    read_it=csv.reader(f)
    list1={}
    l1=[]#这两个列表用于筛选出同时存在日期的值


    list1.setdefault(i,{})
    pathdir.remove(i)
    for row in read_it:
        list1[i].setdefault(row[0],row[3])#第一个是日期 第二个是所对应的值(开盘价)
        l1.append(row[0])
    for ii in pathdir:#第一个文件与其他文件的协方差计算
        l2 = []  # 这两个列表用于筛选出同时存在日期的值
        list1.setdefault(ii, {})
        交集 = []
        f2 = open('C:\\测试提取\\%s' % ii, 'r+')
        read_it2 = csv.reader(f2)
        for row2 in read_it2:
            list1[ii].setdefault(row2[0], row2[3])  # 第一个是日期 第二个是所对应的值(开盘价)
            l2.append(row2[0])
        l1a=set(l1)
        l2a=set(l2)
        交集=list(l1a.intersection(l2a))#得到二者相同的日期
        二者离差积=0
        二者离差积和=0
        协方差=0
        for count,iii in enumerate(交集,1):
            二者离差积=(float(list1[i][iii])-float(dict_information[i]['期望']))*(float(list1[ii][iii])-float(dict_information[ii]['期望']))
            二者离差积和+=二者离差积
        协方差=二者离差积和/count
        dict_information[i]['协方差'].setdefault('cov(%s,%s)'%(i,ii),协方差)
        dict_information[ii]['协方差'].setdefault('cov(%s,%s)'%(ii,i),协方差)
    print('正在计算:%s  %s的协方差'%(i,ii))
zz.write(str(dict_information))
print(dict_information)




