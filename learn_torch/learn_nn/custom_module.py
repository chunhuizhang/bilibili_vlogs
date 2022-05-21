import torch
from torch import nn


class MySeq(torch.nn.Module):
    def __init__(self, *args):
        super().__init__()
        for block in args:
            self._modules[block] = block

    def forward(self, X):
        for block in self._modules.values():
            X = block(X)
        return X


if __name__ == '__main__':
    X = torch.rand(2, 20)
    net = MySeq(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
    net(X)

