import torch
from torch import nn

if __name__ == '__main__':
    rnn = nn.RNN(10, 20, 2)
    input = torch.randn(5, 3, 10)
    h0 = torch.randn(2, 3, 10)
    rnn(input, h0)
