from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("E:/Research_Project/DataSet/0b_decimal/0x260_1.csv")
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
X_test=traindate
y_test=target

model_new=load_model("filter.hdf5")  #加载最好的模型
model_new.evaluate( X_test, y_test)  #计算测试集的val_loss
y_pre=np.squeeze(model_new.predict( X_test))

y_pre=ss.inverse_transform([y_pre])
y_test=ss.inverse_transform(y_test)

print(y_test)
print(y_pre)