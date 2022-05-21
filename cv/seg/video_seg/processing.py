import paddlehub as hub
from PIL import Image
import os
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def video2jpg(video_file, output_path):
    '''
    将视频文件video_file每一帧转成图片保存到output_path文件夹
    '''
    try:
        os.makedirs(output_path)  # 创建输出文件夹
    except:
        print()

    # 读取视频文件
    cap = cv2.VideoCapture(video_file)
    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    num = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}/{}-{}.jpg'.format(output_path, n_frames, num), frame)
            num += 1
        else:
            break
    cap.release()  # 关闭视频


def humanseg(images):


    # 装载模型
    module = hub.Module(name="deeplabv3p_xception65_humanseg")
    # 执行模型segmentation(抠图)命令
    module.segmentation(data={"image": images}, visualization=True)

    # for i, img in enumerate(images):
    #     print(i, img)
    #     result = module.segmentation(data={"image": [img]}, visualization=True)


def file_list(listdir):
    im_list = []
    imgs = os.listdir(listdir)
    for img in imgs:
        im_list.append(os.path.join(listdir, img))
    return im_list


if __name__ == '__main__':
    # video2jpg('vtest.avi', 'v2j')

    img_list = file_list('./v2j')
    humanseg(img_list)
