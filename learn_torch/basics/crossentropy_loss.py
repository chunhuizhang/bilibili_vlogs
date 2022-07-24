
from torch import nn
import torch

if __name__ == '__main__':
    input = torch.randn(3, 5)
    target = torch.empty(3, dtype=torch.long).random_(5)
    loss = nn.CrossEntropyLoss()
    output = loss(input, target)
    print(output)