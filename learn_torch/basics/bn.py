
import torch
from torch import nn


if __name__ == '__main__':
    m = nn.BatchNorm1d(3, momentum=None)
    x1 = torch.randint(0, 5, (2, 3), dtype=torch.float32)
    x2 = torch.randint(0, 5, (2, 3), dtype=torch.float32)

    m(x1)
    print(m.running_mean, m.running_var)
    m(x2)
    print(m.running_mean, m.running_var)

    m.eval()
    x3 = torch.randint(0, 5, (1, 3), dtype=torch.float32)
    m(x3)

