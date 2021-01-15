'''
绘制ID各个变量随时间变化趋势图
'''
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
num=[]
time=[]
df = pd.read_csv('E:/Research_Project/DataSet/0b_decimal/0x329.csv')
num=df.iloc[0:, 0]
arr=num.values
t=round(arr[0],4)

for i in range (len(arr)):
    if i==0:
        t=round(arr[0],4)
    else:
        t=round(t+round(arr[i],4),3)
    time.append(t)

byte1 = [float(i) for i in df.iloc[0:,8]]

plt.plot(time[:1000], byte1[:1000])
plt.xlabel('time')
plt.ylabel('decimal')
plt.show()