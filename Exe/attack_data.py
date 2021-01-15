'''
模拟生成攻击异常数据 
'''
import os
import random
import pandas as pd
import numpy as np

base="E:/Research_Project/DataSet/0b_decimal/test.csv"
df=pd.read_csv(base,encoding='utf-8')

# 模拟洪泛攻击 注入0x00 的周期为0.5ms，随机选择注入的时间，持续长度,攻击的次数

'''random_row=random.randint(1,df.shape[0])
last=df.loc[random_row]
last_time=float("%.5f" % last['timestamp'])
time=last_time+0.0005
flood=pd.DataFrame({'timestamp':[time],
                    'byte1':[00],'byte2':[00],
                    'byte3':[00],'byte4':[00],
                    'byte5':[00],'byte6':[00],
                    'byte7':[00],'byte8':[00]})

df1 = df.loc[:random_row-1]
df2 = df.loc[random_row:]
df1 = df1.append(flood, ignore_index = True)

time=time+0.0005
flood['timestamp']=[time]
df1=df1.append(flood, ignore_index = True)

time=time+0.0005
flood['timestamp']=[time]
df1=df1.append(flood, ignore_index = True)

time=time+0.0005
flood['timestamp']=[time]
df1=df1.append(flood, ignore_index = True)

time=time+0.0005
flood['timestamp']=[time]
df1=df1.append(flood, ignore_index = True)

time=time+0.0005
flood['timestamp']=[time]
df1=df1.append(flood, ignore_index = True)

time2=df2.loc[random_row]['timestamp']+0.003+0.01
df2.loc[random_row,'timestamp']=time2
df=df1.append(df2, ignore_index = True)

df.to_csv('flood.csv',float_format='%.5f')'''

'''模拟重放攻击 Replay attack'''

random_times=random.randint(1,10)
for i in range (random_times):                            #攻击次数
    df_replay=[]
    len=random.randint(1,6)
    ran_start=random.randint(1,df.shape[0])    #开始攻击时间点
    last=df.loc[ran_start]
    last_time=float("%.5f" % last['timestamp'])
    for j in range(len):                       #持续时间     
        replay=last.copy()   
        time=last_time+0.0005*(j+1)                  #重放
        replay.loc['timestamp']=time
        replay.loc['label']=1
        df_replay.append(replay)
        print("..........")
        print(ran_start)
       
    print("********")
    df1 = df.loc[:ran_start]
    df2 = df.loc[ran_start+1:]
    df2.loc[:,'timestamp']=df2.loc[:,'timestamp']+0.0005*(len+1)+0.01 
    df = df1.append(df_replay, ignore_index = True).append(df2, ignore_index = True)

df.to_csv('replay.csv',float_format='%.5f')

'''模拟模糊攻击 Fuzzy attack'''
