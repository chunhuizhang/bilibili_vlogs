# 1、导入模块
import os
import paddlehub as hub
import numpy as np
from collections import Counter
import cv2
import matplotlib.pyplot as plt


path = './data/'
files = os.listdir(path)
imgs = []


for i in files:
    imgs.append(path + i)

cv2.imshow('', cv2.imread(imgs[0]))




# 2、加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')



results = humanseg.segmentation(data={'image':imgs}, visualization=True)
unique, counts = np.unique(results[0]['data'], return_counts=True)
print(dict(zip(unique, counts)))

print()

