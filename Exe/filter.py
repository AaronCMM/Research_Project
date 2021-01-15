import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold

df=pd.read_csv("E:/Research_Project/DataSet/0b_decimal/raw.csv",encoding="gbk")
constant_filter = VarianceThreshold(threshold=0)

#制作数据集

constant_filter.fit(df)
constant_columns=[column for column in df.columns
                  if column not in df.columns[constant_filter.get_support()]]
df.drop(labels=constant_columns,axis=1,inplace=True)

traindate=[]
target=[]
for i in range(6,df.shape[0]):
    tmp=[]
    for j in range(i-6,i):
        tmp.append(list(df.loc[j]))
    traindate.append(tmp)
    target.append(list(df.loc[i]))

traindate=np.array(traindate)
target=np.array(target)
print(traindate.shape)
print(target.shape)