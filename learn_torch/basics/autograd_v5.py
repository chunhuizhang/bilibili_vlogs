
import torch
import math

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
dtype = torch.float

lr = 5e-6

class LegendrePolynomial3(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return 0.5*(5*input**3 - 3*input)
    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        return grad_output*(7.5*input**2 - 1.5)


def train(X, y):
    a = torch.full((), 0, device=device, dtype=dtype, requires_grad=True)
    b = torch.full((), -1, device=device, dtype=dtype, requires_grad=True)
    c = torch.full((), 0, device=device, dtype=dtype, requires_grad=True)
    d = torch.full((), 0.3, device=device, dtype=dtype, requires_grad=True)

    for i in range(2000):
        P3 = LegendrePolynomial3.apply
        # 执行 forward
        y_pred = a + b * P3(c + d*X)
        loss = (y_pred - y).pow(2).sum()
        if i % 100 == 0:
            print('{}/{}: {}'.format(i, 2000, loss.item()))
        # 执行 backward
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
    X = torch.linspace(-math.pi, math.pi, 2000, dtype=dtype, device=device)
    y = torch.sin(X)
    train(X, y)
