'''
数据转十进制，计算时间间隔并转为 ms 单位（原来 s ）
'''
import linecache
arr1=[]
arr2=[]
base_dir="F:/Research_Project/DataSet/"
path=base_dir+"0b/0x4B1.txt"
#path="replaying.txt"
file= open(path)
count=len(file.readlines())
lines=file.readline
file = open(base_dir+"0b_decimal/0x4B1.txt",'a+')
#file=open("replay_2.txt",'a+')
for i in range (count-2):

    fst_line=linecache.getline(path,i+1)
    sec_line=linecache.getline(path,i+2)

    t1=fst_line.split(",",1)[0]
    t2=sec_line.split(",",1)[0]
    b1=fst_line.split(",",1)[1]
    b2=sec_line.split(",",1)[1]
    
    diff=float(t2)*1000-float(t1)*1000
    diff="%.3f" % diff
    s=diff
    num1=[]
    arr1=b2.split(",")
    for num in arr1:
        num=int(num, 16)
        s+=","
        s+=str(num)   
        #num1.append(num)

    file.writelines('\n'+s)