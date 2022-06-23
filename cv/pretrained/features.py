
import timm
import torch
from torch import nn


model_name = 'xception41'
# model_name = 'resnet18'
model = timm.create_model(model_name, pretrained=True)

input = torch.randn(2, 3, 299, 299)

o1 = model(input)
print(o1.shape)

o2 = model.forward_features(input)
print(o2.shape)