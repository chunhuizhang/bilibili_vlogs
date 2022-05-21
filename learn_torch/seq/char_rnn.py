
from io import open
import glob
import os
import unicodedata
import string
import torch
from torch import nn


def find_files(path):
    return glob.glob(path)


def uni_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn' and c in all_letters)


def build_vocab(filepath):
    def read_lines(filename):
        lines = open(filename, encoding='utf-8').read().strip().split('\n')
        return [uni_to_ascii(line) for line in lines]

    category_lines = {}
    all_categories = []

    for filename in find_files(filepath):
        category = os.path.splitext(os.path.basename(filename))[0]
        lines = read_lines(filename)
        all_categories.append(category)
        category_lines[category] = lines
    return category_lines, all_categories


def letter_to_index(letter):
    return all_letters.index(letter)


def letter_to_tensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letter_to_index(letter)] = 1
    return tensor


def line_to_tensor(line):
    tenor = torch.zeros(len(line), 1, n_letters)
    for i, letter in enumerate(line):
        tenor[i][0] = letter_to_tensor(letter)
    return tenor


class RNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = torch.nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = torch.nn.Linear(input_size + hidden_size, output_size)
        self.softmax = torch.nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def init_hidden(self):
        return torch.zeros(1, self.hidden_size)


def category_from_output(output):
    top_v, top_i = output.topk(1)
    category_i = top_i[0].item()
    return category_i, all_categories[category_i], top_v.item()


def train(x, y):
    hidden = rnn.init_hidden()
    rnn.zero_grad()
    for i in range(x.shape[0]):
        output, hidden = rnn.forward(x[i], hidden)
    loss = criterion(output, y)
    loss.backward()
    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-lr)
    return output, loss.item()


if __name__ == '__main__':
    all_letters = string.ascii_letters + " .,;'"
    n_letters = len(all_letters)

    category_lines, all_categories = build_vocab('../text_data/names/*.txt')

    n_categories = len(all_categories)
    n_hidden = 128
    rnn = RNN(n_letters, n_hidden, n_categories)
    lr = 1e-5
    criterion = torch.nn.NLLLoss()

    nn.CrossEntropyLoss()

