
import timm
import torch
from torch import nn


def print_shape(m, i, o):
    #m: module, i: input, o: output
    # print(m, i[0].shape, o.shape)
    print(i[0].shape, m,  o.shape)


def get_children(model: nn.Module):
    # get children form model!
    children = list(model.children())
    flatt_children = []
    if children == []:
        # if model has no children; model is last child! :O
        return model
    else:
       # look for children from children... to the last child!
       for child in children:
            try:
                flatt_children.extend(get_children(child))
            except TypeError:
                flatt_children.append(get_children(child))
    return flatt_children


# model_name = 'vgg11'
model_name = 'resnet34'
model = timm.create_model(model_name, pretrained=True)

flatt_children = get_children(model)
for layer in flatt_children:
    layer.register_forward_hook(print_shape)

# for layer in model.children():
#     layer.register_forward_hook(print_shape)

# 4d: batch*channel*width*height
batch_input = torch.randn(4, 3, 300, 300)

model(batch_input)
