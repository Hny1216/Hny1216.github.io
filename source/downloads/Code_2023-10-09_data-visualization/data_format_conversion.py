#encoding=gbk
from glob import glob
from tqdm import tqdm
import pkl2mat
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

date_category1 = ['data/battery_brand1','data/battery_brand2','data/battery_brand3']
date_category2 = ['/train','/test','/data']
matrix = [[1,1,0],[1,1,0],[0,0,1]]

## 创建转换后的数据文件夹树
folder_name, add_name = 'trans_data', 'trans_'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    for i in range(3):
        os.mkdir(add_name + date_category1[i])
        for j in range(3):
            if matrix[i][j]: os.mkdir(add_name + date_category1[i] + date_category2[j])
else: pass

## 转换数据格式
for i in range(3):
    for j in range(3):
        if matrix[i][j]:
            input_path = glob(date_category1[i] + date_category2[j] + '/*.pkl')
            for each_path in tqdm(input_path):
                output_path = 'trans_' + each_path
                pkl2mat.pkl2mat(each_path, output_path)
