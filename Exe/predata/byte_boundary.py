'''
寻找连续字节对，字节边界 论文"READ '方法复现
2020-08-08
'''
import math
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DLC=64
f=open("F:/Research_Project/DataSet/0b_decimal/0x329_Byte_test.txt")
lines = f.readlines()
msg_list=[x.strip() for x in lines]  # strip() 去除字符串头尾空格
#msg_list=[x.strip() for x in lines]
print(len(msg_list))

def pre_processing(messageList, DLC):
    payload_len=len(messageList)
    bitflip=[0]*DLC
    magnitude=[0]*DLC
    pre=messageList[0]
    for item in messageList :
        for ix in range(0,DLC):      #range函数，左闭右开
            if item[ix]!=pre[ix]:
                bitflip[ix]+=1    
        pre=item

    for ix in range(0,DLC):
        bitflip[ix]=round(bitflip[ix]/payload_len,3) 
        if(bitflip[ix]!=0):
            #print(math.log10(bitflip[ix]))
            magnitude[ix]=math.ceil(math.log10(bitflip[ix]))           # log向上取整
        else:
            magnitude[ix]=float('-inf')
    print("bitflip",bitflip)
    print("magnitude",magnitude)

    return bitflip,magnitude

'''phase1 大致划分'''
def phase1(magnitude,DLC):
    print("phase1")
    ref=[]
    pre_mag=bitflip[0]
    #pre_mag=magnitude[0]
    ixS=0                                     #起始位置bit索引

    for ix in range(1,DLC):
        if magnitude[ixS]==float('-inf'): 
            ixS+=1
   
        while magnitude[ix]==float('-inf') and magnitude[ix-1]==float('-inf'):
            if ix+1!=DLC:
                ix+=1
                ixS=ix
      
        if magnitude[ix]==float('-inf')and magnitude[ix-1]!=float('-inf')and magnitude[ix+1]!=float('-inf'): 
            ref.append([ixS,ix-1]) 
            ixS=ix
        elif bitflip[ix]<pre_mag:
            ref.append([ixS,ix-1])      #存储连续字节对的起始、终止位置索引
            ixS=ix
        pre_mag=bitflip[ix]
    ref.append([ixS,DLC-1])
    print("-------------------")
    print("ref: ",ref)
    return ref

def match_counter(ixS,ixE):
    init=ixE-1
    flag=False
    while init>=ixS:
        if math.isclose(2*bitflip[init],bitflip[init+1],rel_tol=0.01):
            init = init - 1
            flag=True
        else: break
    return init,flag

def phase2(ref,bitflip):
    rRef=[]

    for sign in ref:
        ixS=sign[0]
        ixE=sign[1]
        
        if magnitude[ixE]==0:
            init,flag=match_counter(ixS,ixE)
            if flag:
                rRef.append([ixS,init,'Physical'])
                rRef.append([init+1,ixE,'Counter'])
            else:
                exit=False
                for i in range(ixS,ixE) :
                    if not exit:
                        idx=bitflip[i:ixE+1]
                        mean=np.mean(idx)
                        std=np.std(idx)
                        if all(magnitude[i:ixE+1])==0 and (0.5 - std <= mean <= 0.5 + std):
                            if i!=ixS:rRef.append([ixS,i-1,'Physical'])
                            rRef.append([i,ixE,'CRC'])
                            exit=True
                if not exit:
                    rRef.append([ixS,ixE,'Physical'])
        else:
            rRef.append([ixS,ixE,'Physical'])   
    return rRef

bitflip,magnitude=pre_processing(msg_list,DLC)
#ref=phase1(magnitude,DLC)
ref=[[0,1],[3,7],[43,47],[50,55]]
rRef=phase2(ref,bitflip)
print("rRef: ",rRef)

'''绘制连续字节对相应的时序变化'''
'''
for item in rRef:
    x=[]
    y=[]
    nums=[]
    ixS=item[0]
    ixE=item[1]
    title=item[2]
    if ixS>=ixE: 
        continue

#取出二进制索引对，对应的十进制值
    for msg in msg_list:
        number = int(msg[ixS:ixE + 1],2)
        nums.append(number)
    for i in range(len(msg_list)):
            x.append(i)
    plt.title(title)
    plt.xlabel('count')
    plt.ylabel('decimal')
    plt.plot(x, nums)
    plt.show()
'''
'''
    for i in range(ixS,ixE+1):                # 绘制连续字节对，对应的翻转率变化趋势
        x.append(i)
        y.append(bitflip[i])
    
    plt.xlabel('bit')
    plt.ylabel('bitflip')
    plt.plot(x, y)
    plt.show()
'''

#合成数据集
'''
nums=[]
#ixS=rRef[3][0]
ixS=42
ixE=55
#ixE=rRef[3][1]
data = pd.read_csv(r'File_Classify.csv')
for msg in msg_list:
    number = int(msg[ixS:ixE + 1],2)
    nums.append(number)      
data['Physical_5']=nums
    #dataframe = pd.DataFrame(data)
data.to_csv(r'File_Classify_1.csv',mode='a',index =False)
'''


nums_0=[]
ixS_0=rRef[2][0]
ixE_0=rRef[2][1]

nums_1=[]
ixS_1=rRef[3][0]
ixE_1=rRef[3][1]
'''
nums_2=[]
ixS_2=rRef[2][0]
ixE_2=rRef[2][1]

nums_3=[]
ixS_3=rRef[4][0]
ixE_3=rRef[4][1]
'''
for msg in msg_list:
    number = int(msg[ixS_0:ixE_0 + 1],2)
    n_1=int(msg[ixS_1:ixE_1 + 1],2)
    #n_2=int(msg[ixS_2:ixE_2 + 1],2)
    #n_3=int(msg[ixS_3:ixE_3 + 1],2)
    
    nums_0.append(number) 
    nums_1.append(n_1) 
    #nums_2.append(n_2) 
    #nums_3.append(n_3) 

#data = {'Physic_1':nums_0,'Physic_2':nums_1,'Physic_3':nums_2,'Physic_4':nums_3}
data = {'Physic_1':nums_0,'Physic_2':nums_1}
dataframe = pd.DataFrame(data)
dataframe.to_csv(r'File_329.csv',columns=['Physic_1','Physic_2'])
