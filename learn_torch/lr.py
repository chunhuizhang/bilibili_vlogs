
import numpy as np
import torch
import torch.nn as nn
from torch.autograd import Variable
from torch import optim
import matplotlib.pyplot as plt



def gen_data():
    x_train = np.asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                          7.042, 10.791, 5.313, 7.997, 3.1], dtype=np.float32)
    y_train = np.asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221, 2.827,
                          3.465, 1.65, 2.904, 1.3], dtype=np.float32)
    assert x_train.shape == y_train.shape
    n = x_train.shape[0]
    x_train = x_train.reshape((n, -1))
    y_train = y_train.reshape((n, -1))
    return x_train, y_train


class LinearRegression(nn.Module):
    def __init__(self, in_size, out_size):
        super(LinearRegression, self).__init__()
        self.linear_fn = nn.Linear(in_size, out_size)

    def forward(self, x):
        return self.linear_fn(x)


if __name__ == '__main__':
    x_train, y_train = gen_data()
    lr = 1e-3
    n_epoch = 500
    # build
    in_size, out_size = x_train.shape[-1], y_train.shape[-1]
    model = LinearRegression(in_size, out_size)
    criterion = nn.MSELoss()

    opt = optim.SGD(model.parameters(), lr=lr)

    # train
    for epoch in range(n_epoch):
        inputs = Variable(torch.from_numpy(x_train))
        outputs = Variable(torch.from_numpy(y_train))
        opt.zero_grad()
        preds = model(inputs)
        loss = criterion(outputs, preds)
        loss.backward()
        opt.step()
        if (epoch + 1) % 50 == 0:
            # print(loss.data)
            print('{}/{}, loss:{}'.format(epoch, n_epoch, loss.data))

    print(model.state_dict())
    y_pred = model(Variable(torch.from_numpy(x_train))).data.numpy()
    plt.plot(x_train, y_train, 'ro')
    plt.plot(x_train, y_pred)
    plt.show()
