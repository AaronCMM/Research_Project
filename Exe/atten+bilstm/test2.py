from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from create_traindate import X_test,y_test,ss

model_new=load_model("model/0x316_1.hdf5") 
model_new.evaluate( X_test, y_test)  
y_pre=np.squeeze(model_new.predict( X_test))

y_pre=ss.inverse_transform(y_pre)
y_test=ss.inverse_transform(y_test)

for i in range(6):
    print (i,"条数据")
    plt.figure(figsize=(24,8))
    real, = plt.plot(y_test[:,i][:100], c='red',label='real')
    predict, = plt.plot(y_pre[:,i][:100], c='g',label='predict')
    plt.legend(handles=[real,predict])
    plt.show()
    plt.close()

'''plt.figure(figsize=(24,8))
plt.plot(y_test[:,0][15:60], c='red')
plt.plot(y_pre[15:60], c='g')
plt.show()
plt.close()'''

'''print(X_test)
print(y_test)
print(y_pre)'''