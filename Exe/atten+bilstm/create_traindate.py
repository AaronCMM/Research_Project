import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

# 读取数据
df=pd.read_csv("E:/Research_Project/DataSet/0b_decimal/0x316_1.csv",encoding="gbk")
constant_filter = VarianceThreshold(threshold=0)
constant_filter.fit(df)
constant_columns=[column for column in df.columns
                if column not in df.columns[constant_filter.get_support()]]
df.drop(labels=constant_columns,axis=1,inplace=True)

'''数据预处理'''
ss=MinMaxScaler()
ss.fit(df)
df=pd.DataFrame(ss.transform(df))

#制作数据集
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
print(traindate.shape[0])
print(traindate.shape[1])

X_train,X_test,y_train,y_test=train_test_split(traindate,target,test_size=0.2)
