# -*- coding: utf-8 -*-
import h5py  # 导入工具包
import numpy as np
 
# HDF5的读取：
with h5py.File('F:/Research_Project/DataSet/Driver1_Trip1.hdf', 'r') as f:
    print(f["CAN/Yawrate1"])   
    for group in f:
        #print(group)
        group_read=f[group]
        print("********************")
        for subgroup in group_read:
        #    print (subgroup) 
            dset_read = f[group+'/'+subgroup] 
           # print(dset_read)                          
        '''
            for dset in dset_read:
            #获取dataset数据
                dset1 = f[group+'/'+subgroup+'/'+dset]
                print (dset1.name)
                data = np.array(dset1)
                print (data.shape)
                x = data[...,0]
                y = data[...,1]        
        '''