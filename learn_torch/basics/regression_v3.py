import math
import torch


dtype = torch.float
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'


lr = 1e-6


def train(X, y):
    a = torch.randn((), device=device, dtype=dtype, requires_grad=True)
    b = torch.randn((), device=device, dtype=dtype, requires_grad=True)
    c = torch.randn((), device=device, dtype=dtype, requires_grad=True)
    d = torch.randn((), device=device, dtype=dtype, requires_grad=True)

    for i in range(2000):
        y_pred = a + b*X + c*X**2 + d*X**3
        loss = (y_pred - y).pow(2).sum()
        if i % 100 == 0:
            print('{}/{}: {}'.format(i, 2000, loss.item()))
        loss.backward()
        with torch.no_grad():
            a -= lr * a.grad
            b -= lr * b.grad
            c -= lr * c.grad
            d -= lr * d.grad
            a.grad = None
            b.grad = None
            c.grad = None
            d.grad = None
    print('a = {}, b = {}, c = {}, d = {}'.format(a.item(), b.item(), c.item(), d.item()))

if __name__ == '__main__':

    X = torch.linspace(-math.pi, math.pi, 2000)
    y = torch.sin(X)
    train(X, y)

