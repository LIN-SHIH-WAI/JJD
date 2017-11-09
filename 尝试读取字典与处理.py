#__author:"LIN SHIH-WAI"
#date:  2017/11/9
with open('记录.txt','r+',encoding='utf-8') as f:
    read_it=f.read()
    dict_information=eval(read_it)

print(type(dict_information))
print(dict_information['600000.csv'])
print('一共有多少个股票:',len(dict_information))#总共有多少个数据
for i in dict_information:#获取所有的字典数量
    dict_information[i]['协方差'].setdefault('cov(%s,%s)'%(i,i),float(dict_information[i]['方差']))
    print('股票:',i,'有多少个协方差',print(len(dict_information[i]['协方差'])))
    