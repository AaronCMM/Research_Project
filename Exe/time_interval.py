'''
探索 时间间隔的变化，证明ECU消息存在周期性
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

num=[]
base_dir="E:/Research_Project/DataSet/"
f=open(base_dir+"pdata_decimal/0316.txt")
for line in f:
    a=line.split(',',1)
    num.append(float(a[0]))
cout= np.arange(5000)
num=num[:5000]
avg= sum(num) / len(num)
print("平均",avg)

plt.scatter(cout, num, color='blue', marker='.')
plt.xlabel('count')
plt.ylabel('interval[ms]')

plt.show()