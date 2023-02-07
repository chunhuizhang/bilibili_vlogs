import torch
from torch import nn
import torchvision
from torchvision import transforms


train_dataset = torchvision.datasets.FashionMNIST(root='../data',
                                           train=True,
                                           download=True,
                                           transform=transforms.ToTensor())
test_dataset = torchvision.datasets.FashionMNIST(root='../data',
                                          train=False,
                                          download=True,
                                          transform=transforms.ToTensor())

train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

for batch_index, (images, labels) in enumerate(train_dataloader):
    if batch_index == len(train_dataset)//64:
        print(images.shape, labels.shape)
