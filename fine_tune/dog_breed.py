import torch,os,torchvision
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset
from torchvision import datasets, models, transforms
from PIL import Image
from sklearn.model_selection import StratifiedShuffleSplit
from torchviz import make_dot
from datetime import datetime
from tqdm import tqdm


DATA_ROOT = './data/dog-breed-identification'



from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


class DogDataset(Dataset):
    def __init__(self, labels_df, img_path, transform=None):
        self.labels_df = labels_df
        self.img_path = img_path
        self.transform = transform

    def __len__(self):
        return self.labels_df.shape[0]

    def __getitem__(self, idx):
        image_name = os.path.join(self.img_path, self.labels_df.id[idx]) + '.jpg'
        img = Image.open(image_name)
        label = self.labels_df.label_idx[idx]

        if self.transform:
            img = self.transform(img)
        return img, label

@timing
def train(model,device, train_loader, epoch):
    model.train()
    for batch_idx, data in tqdm(enumerate(train_loader)):
        print('{}: {}/{}, {}'.format(epoch, batch_idx, len(train_dataset), data[0].shape))
        x,y= data
        x=x.to(device)
        y=y.to(device)
        optimizer.zero_grad()
        y_hat= model(x)
        loss = criterion(y_hat, y)
        loss.backward()
        optimizer.step()
    print ('Train Epoch: {}\t Loss: {:.6f}'.format(epoch,loss.item()))


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for i,data in enumerate(test_loader):
            x,y= data
            x=x.to(device)
            y=y.to(device)
            optimizer.zero_grad()
            y_hat = model(x)
            test_loss += criterion(y_hat, y).item() # sum up batch loss
            pred = y_hat.max(1, keepdim=True)[1] # get the index of the max log-probability
            correct += pred.eq(y.view_as(pred)).sum().item()
    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(val_dataset),
        100. * correct / len(val_dataset)))


if __name__ == '__main__':

    all_labels_df = pd.read_csv(os.path.join(DATA_ROOT, 'labels.csv'))
    breeds = all_labels_df.breed.unique()
    breed2idx = dict((breed, idx) for idx, breed in enumerate(breeds))
    idx2breed = dict((idx, breed) for idx, breed in enumerate(breeds))
    # all_labels_df['label_idx'] = [breed2idx[b] for b in all_labels_df.breed]
    all_labels_df['label_idx'] = all_labels_df['breed'].apply(lambda x: breed2idx[x])
    print(all_labels_df.head())

    model_ft = models.resnet50(pretrained=True)
    models.resnet18()
    print(model_ft)
    # make_dot(yhat, params=dict(list(model_ft.named_parameters()))).render("resnet50_torchviz", format="png")

    IMG_SIZE = 224  # resnet50的输入是224的所以需要将图片统一大小
    BATCH_SIZE = 256  # 这个批次大小需要占用4.6-5g的显存，如果不够的化可以改下批次，如果内存超过10G可以改为512
    IMG_MEAN = [0.485, 0.456, 0.406]
    IMG_STD = [0.229, 0.224, 0.225]
    CUDA = torch.cuda.is_available()
    DEVICE = torch.device("cuda" if CUDA else "cpu")

    train_transforms = transforms.Compose([
        transforms.Resize(IMG_SIZE),
        transforms.RandomResizedCrop(IMG_SIZE),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(30),
        transforms.ToTensor(),
        transforms.Normalize(IMG_MEAN, IMG_STD)
    ])

    val_transforms = transforms.Compose([
        transforms.Resize(IMG_SIZE),
        transforms.CenterCrop(IMG_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(IMG_MEAN, IMG_STD)
    ])

    dataset_names = ['train', 'valid']
    stratified_split = StratifiedShuffleSplit(n_splits=1, test_size=0.1, random_state=0)
    train_split_idx, val_split_idx = next(iter(stratified_split.split(all_labels_df.id, all_labels_df.breed)))
    train_df = all_labels_df.iloc[train_split_idx].reset_index()
    val_df = all_labels_df.iloc[val_split_idx].reset_index()
    # print(len(train_df))
    # print(len(val_df))

    image_transforms = {'train': train_transforms, 'valid': val_transforms}

    train_dataset = DogDataset(train_df, os.path.join(DATA_ROOT, 'train'), transform=image_transforms['train'])
    val_dataset = DogDataset(val_df, os.path.join(DATA_ROOT, 'train'), transform=image_transforms['valid'])
    image_dataset = {'train': train_dataset, 'valid': val_dataset}

    image_dataloader = {x: DataLoader(image_dataset[x], batch_size=BATCH_SIZE, shuffle=True, num_workers=0) for x in
                        dataset_names}
    dataset_sizes = {x: len(image_dataset[x]) for x in dataset_names}

    # batch = next(iter(train_dataset))
    # yhat = model_ft(batch[0].unsqueeze(0))
    # make_dot(yhat).render("resnet_ft")

    # 将所有的参数层进行冻结
    for param in model_ft.parameters():
        param.requires_grad = False
    # 这里打印下全连接层的信息
    print(model_ft.fc)
    num_fc_ftr = model_ft.fc.in_features  # 获取到fc层的输入
    model_ft.fc = nn.Linear(num_fc_ftr, len(breeds))  # 定义一个新的FC层
    model_ft = model_ft.to(DEVICE)  # 放到设备中
    print(model_ft)  # 最后再打印一下新的模型

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam([
        {'params': model_ft.fc.parameters()}
    ], lr=0.001)  # 指定 新加的fc层的学习率

    model_parameters = filter(lambda p: p.requires_grad, model_ft.parameters())
    params = sum([np.prod(p.size()) for p in model_parameters])
    print('params: {}, start time: {}'.format(params, datetime.now()))
    for epoch in range(1, 10):
        train(model=model_ft, device=DEVICE, train_loader=image_dataloader["train"], epoch=epoch)
        test(model=model_ft, device=DEVICE, test_loader=image_dataloader["valid"])
