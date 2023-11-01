import pickle
import numpy as np
import pandas as pd
from scipy import io
import torch
from glob import glob
from tqdm import tqdm
from collections import OrderedDict

def get_index(filename:str):
    f = torch.load(filename)
    infor = f[1]
    index1,index2 = filename.rfind('\\'),filename.rfind('.pkl')
    return infor['car'],[infor['charge_segment'], filename[index1+1:index2]]


data_category1 = ['data/battery_brand1','data/battery_brand2','data/battery_brand3']
data_category2 = ['/train','/test','/data']
matrix = [[1,1,0],[1,1,0],[0,0,1]]

## 数据编号
for i in range(3):
    data_order = {}
    for j in range(3):
        if matrix[i][j]:
            input_path = glob(data_category1[i] + data_category2[j] + '/*.pkl')
            for each_path in tqdm(input_path):
                car_index, infor = get_index(each_path)
                if car_index in list(data_order.keys()):
                    data_order[car_index].append(infor)
                else:
                    data_order[car_index] = [infor]
    torch.save(data_order,data_category1[i]+'/data_distribution.pkl')

## pkl2mat
for i in range(3):
    input_path = data_category1[i]+'/data_distribution.pkl'
    data = torch.load(input_path)
    data_save = []
    car_index = list(data.keys())
    car_index.sort()
    for car in car_index:
        data_save2 = np.empty((2,),np.object_)
        data_save2[0] = car
        data_save2[1] = np.array(data[car],dtype=np.object_)
        data_save.append(data_save2)
    io.savemat('trans_'+data_category1[i]+'/data_distribution.mat',{'data_distribution':data_save})



