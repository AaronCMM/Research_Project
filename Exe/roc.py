import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,auc
import numpy as np
import xlrd

"""
主函数
"""   

if __name__ == '__main__':
    stats_roc = xlrd.open_workbook("test.xlsx")
    sheet1 = stats_roc.sheets()[0]; #获取sheet1
    size = sheet1.nrows; #获取行数
    y_Actual = sheet1.col_values(0) [1:size]; #获取标签，第0行是标题，数据从第一行开始
    y_Predicted = sheet1.col_values(1) [1:size]; #获取预测值（置信度）
    size = size - 1;#因为第零行为标题，舍去
    
    threshold = 0;#阈值
    TPR_list = []; #ROC 的纵坐标 真阳率
    FPR_list = []; #ROC 的横坐标 假阳率
    
    
    while threshold < 1.005: # 设置阈值
        y_Predicted_new = []
        for i in range(0,size): #二分法重置预测值
            if y_Predicted[i] >= threshold:
                y_Predicted_new.append(1)
            else :
                y_Predicted_new.append(0)
        cm = confusion_matrix(y_Actual, y_Predicted_new) ; #混淆矩阵
            
        TP = cm[1,1]
        TN = cm[0,0]
        FP = cm[0,1]
        FN = cm[1,0]
        FPR = round(FP / (FP + TN),3);#保留小数点后三位
        TPR = round(TP / (TP + FN),3)
        TPR_list.append(TPR); 
        FPR_list.append(FPR)
        
        threshold += 0.005
        #while 结束
        
    #作图   
    '''plt.figure()
    plt.plot(FPR_list, TPR_list, color='green')  
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Comparison of classification models')
    plt.show()
    plt.close()'''

    tpr=np.array([0,0.1,0.3,0.5,0.73,0.82,0.93,1,1,1])
    fpr=np.array([0,0.008,0.01,0.04,0.07,0.09,0.12,0.17,0.66,1]) 
    roc_auc=auc(fpr,tpr)

    print("AUC : ", roc_auc)
        