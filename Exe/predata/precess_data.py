import os
import numpy as np

arr=[]
base="F:/Research_Project/DataSet/CAN/"
file= open(base+"15.txt")
for line in file :
    a=line.split(',',3)
    time=a[0]
    id=a[1] 
    bit=a[3]
    if id not in arr:
        arr.append(id)
    if id=="0x4B1":   
        path="F:/Research_Project/DataSet/0b/"
        filename=path+id+".txt"

        f=open(filename,'a+')
        str=time+","+bit
        f.writelines(str) 