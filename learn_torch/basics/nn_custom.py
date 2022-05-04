
import torch
import math


device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
dtype = torch.float
lr = 1e-3


class Poly3(torch.nn.Module):
    def __init__(self):
        super(Poly3, self).__init__()
        self.a = torch.nn.Parameter(torch.randn(()))
        self.b = torch.nn.Parameter(torch.randn(()))
        self.c = torch.nn.Parameter(torch.randn(()))
        self.d = torch.nn.Parameter(torch.randn(()))

    def forward(self, x):
        return self.a + self.b * x + self.c * x**2 + self.d * x**3

    def __repr__(self):
        return f'y = {self.a.item()} + {self.b.item()} x + {self.c.item()} x^2 + {self.d.item()} x^3'


def train(X, y):
    for i in range(2000):
        y_pred = model(X)
        loss = loss_fn(y_pred, y)

        if i % 100 == 0:
            print('{}/{}: {}'.format(i, 2000, loss.item()))

        # model.zero_grad()
        opt.zero_grad()

        loss.backward()

        # with torch.no_grad():
        #     for param in model.parameters():
        #         param -= lr * param.grad
        opt.step()


if __name__ == '__main__':

    X = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
    y = torch.sin(X)

    # p = torch.Tensor([1, 2, 3])
    # X = X.unsqueeze(-1).pow(p)

    # model = torch.nn.Sequential(
    #     torch.nn.Linear(3, 1),
    #     torch.nn.Flatten(0, 1)
    # )
    model = Poly3()

    loss_fn = torch.nn.MSELoss(reduction='sum')
    opt = torch.optim.RMSprop(model.parameters(), lr=lr)

    train(X, y)
    # weight_layer = model[0]
    #
    # print('y = {} + {}x + {}x^2 + {}x^3'.format(weight_layer.bias.item(),
    #                                             weight_layer.weight[0, 0].item(),
    #                                             weight_layer.weight[0, 1].item(),
    #                                             weight_layer.weight[0, 2].item()))
    print(model)
