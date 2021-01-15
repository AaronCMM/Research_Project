'''
转二进制
'''
import numpy as np
base_dir="F:/Research_Project/DataSet/"
file = open(base_dir+"0b/0x002.txt")
f=open(base_dir+"0b_decimal/0x002_Byte.txt",'a+')
for line in file :
    b1=line.split(",",1)[1]
    num1=[]
    arr1=b1.split(",")
    for x in arr1:
        #x=bin(int(x,16))[2:]
        x='{:08b}'.format(int(x,16))
        f.writelines(x)    
    f.writelines('\n')
