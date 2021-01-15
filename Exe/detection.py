'''
最终异常检测系统；时间间隔+数据域预测 相结合
'''
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from threshold import the
import matplotlib.pyplot as plt
from sklearn import metrics  
from sklearn.metrics import confusion_matrix,accuracy_score,auc
from scipy.interpolate import make_interp_spline

df=pd.read_csv("replay_2.csv",encoding="gbk")
df.drop(labels=['byte5','byte4'],axis=1,inplace=True)

df_time=pd.DataFrame(df[df.columns[0]])
df_data=pd.DataFrame(df[df.columns[1:6]])
df_label=pd.DataFrame(df[df.columns[7]])

'''ss=MinMaxScaler()
ss.fit(df_data)
df_data=pd.DataFrame(ss.transform(df_data))

model_new=load_model("model/filter.hdf5")'''

y_pre=[]
y_true=[]
TPR_list = []; 
FPR_list = []; 

for i in range(6,df.shape[0]):
    tmp1=[]               #时间间隔
    y_true.append(df_label.loc[i])
    if(df_time.loc[i]['timestamp']>12 or df_time.loc[i]['timestamp']==0.5):    #
        y_pre.append(1)
    else:
        y_pre.append(0)

#fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pre)  

'''ROC曲线图绘制'''
'''tpr=np.array([0,0.22,0.49,0.72,0.86,0.94,1,1,1])
fpr=np.array([0,0.002,0.01,0.04,0.07,0.1,0.13,0.42,1]) 

tpr_b=np.array([0,0.1,0.18,0.34,0.45,0.57,0.63,0.76,0.84,0.93,1,1,1])
fpr_b=np.array([0,0.02,0.08,0.15,0.23,0.27,0.34,0.41,0.49,0.52,0.57,0.63,1])

tpr_t=np.array([0,0.12,0.12,0.22,0.22,0.34,0.34,0.42,0.42,0.55,0.55 ,0.63 ,0.63 ,0.7,0.7,0.86,0.86,0.95,0.95,1,1,1])
fpr_t=np.array([0,0.028,0.06,0.06,0.17,0.17,0.25,0.25,0.42,0.42,0.46,0.46,0.51,0.51,0.63,0.63,0.71,0.71,0.75,0.75,0.8,1])

roc_auc = auc(fpr, tpr) 
roc_auc_b=auc(fpr_b,tpr_b)
roc_auc_t=auc(fpr_t,tpr_t)

print(accuracy_score(y_true, y_pre))

plt.subplots(figsize=(7,5.5));
plt.plot(fpr, tpr, color='darkorange',
         lw=2, label='T+BiLSTM (auc: %0.2f)' % roc_auc);

plt.plot(fpr_b, tpr_b, color='blue',
         lw=2, label='BiLSTM (auc : %0.2f)' % roc_auc_b);

plt.plot(fpr_t, tpr_t, color='green',
         lw=2, label='T (auc : %0.2f)' % roc_auc_t);

plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--');
plt.xlim([0.0, 1.0]);
plt.ylim([0.0, 1.05]);
plt.xlabel('False Positive Rate');
plt.ylabel('True Positive Rate');
plt.title('ROC Curve');
plt.legend(loc="lower right");
#plt.savefig("temper_2")
plt.show()'''