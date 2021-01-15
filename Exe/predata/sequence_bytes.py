'''
寻找连续字节对，并绘制图
'''
import matplotlib.pyplot as plt
import sys
import numpy as np
import pylab

f=open("E:/Research_Project/DataSet/0b_decimal/0x260_byte/0x260_Byte_test.txt")
content_list = f.readlines()
num=[x.strip() for x in content_list]  # strip() 去除 字符串 头尾空格

xor = []
for i in range(len(num)-1):
    x=[]
    for k in range (len(num[i])):
        n1=(num[i])[k]               # num[i] 表示第i行
        n2=(num[i+1])[k]
        x.append(int(n1)^int(n2))
    xor.append(x)
#print(xor)

'''得到从低位到高位(从右往左)的TANG数组'''
TANG = [None] * 64
for index in range(len(TANG)):
    count = 0
    for i in xor:
        if i[len(i) - index - 1] == 1:
            count += 1 
    TANG[index] = count
print("TANG:", TANG)

''' 找出从低位到高位的索引对 算法'''
clusters = []
left = 0
right = left
while right < len(TANG):
    cluster = []
    if TANG[left] == 0:
        left += 1
    else:
        cluster.append(left)
        right = left + 1
        while right < len(TANG) and  TANG[right] - TANG[right - 1] <= 300 and TANG[right] != 0:
            right += 1
        cluster.append(right - 1)
        clusters.append(cluster)
        left = right
    right = left
 
print("clusters:", clusters)
#clusters=[[0,3],[4,7],[8,15],[16,21],[40,47],[48,55],[56,63]]
 
''' 找出索引对对应的值'''
start = 63 - clusters[0][1]
end = 63 - clusters[0][0]
# 存储有效位的值
nums=[]
for i in num:
    #print(i)
    number = int(i[start:end + 1], 2)
    nums.append(number)

resultNum = nums

#保存1000的数量,保存在numResult中
numResult = []
countNum = 0
for i in resultNum:
    if countNum == 3000:
        break
    numResult.append(i)
    countNum += 1
print(".....................")
print(len(numResult))
numResult = numResult[:200]

''' 画出索引对对应的值'''
fig, ax = plt.subplots()
lst = [n for n in range(0, 200)]
# 设置横坐标名称
plt.xlabel('Message')
# 设置纵坐标名称
plt.ylabel('Decimal Value')
plt.plot(lst, numResult)
plt.show()
