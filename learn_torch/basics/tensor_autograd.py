
import torch
import math
import numpy as np


device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float

# a = torch.randn((), device=device, dtype=dtype)
# b = torch.randn((), device=device, dtype=dtype)
# c = torch.randn((), device=device, dtype=dtype)
# d = torch.randn((), device=device, dtype=dtype)
# params = [a, b, c, d]

lr = 1e-6


def train(X, y):
    a = torch.randn((), device=device, dtype=dtype)
    b = torch.randn((), device=device, dtype=dtype)
    c = torch.randn((), device=device, dtype=dtype)
    d = torch.randn((), device=device, dtype=dtype)

    for i in range(2000):
        y_pred = a + b*X + c*X**2 + d*X**3
        loss = (y_pred - y).pow(2).sum().item()
        if i % 50 == 0:
            print(i, loss)
        loss_grad = 2*(y_pred - y)
        a_grad = loss_grad.sum()
        b_grad = (loss_grad * X).sum()
        c_grad = (loss_grad * X**2).sum()
        d_grad = (loss_grad * X**3).sum()
        # if i % 50 == 0:
        #     print(a_grad, b_grad, c_grad, d_grad)

        a -= lr * a_grad
        b -= lr * b_grad
        c -= lr * c_grad
        d -= lr * d_grad
    print('a = {}, b = {}, c = {}, d = {}'.format(a.item(), b.item(), c.item(), d.item()))

if __name__ == '__main__':
    X = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=torch.float)
    y = torch.sin(X)
    train(X, y)



