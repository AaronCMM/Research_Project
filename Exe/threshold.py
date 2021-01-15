'''
阈值计算 求均值、方差
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

base_dir="E:/Research_Project/DataSet/"
path=base_dir+"0b_decimal/0x260_time.csv"
df=pd.read_csv(path,encoding="gbk")
df_time=pd.DataFrame(df[df.columns[0]])
df_time=df_time['timestamp']

# 均值计算
#print(df_time.shape[0])
num=[]
for i in range(df_time.shape[0]):
    num.append(df_time.loc[i])

avg=np.mean(num)
avg=float("%.3f" % avg)

# 标准差计算
std=np.std(num, ddof =0)
std=float("%.3f"%std)

'''FPR计算'''
k=1
threshold=avg+4*std
the=float("%.3f"%threshold)
'''print(avg)
print(std)
print(the)'''