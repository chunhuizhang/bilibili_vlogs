import torch
from torch import nn


def t1():
    rnn = nn.RNN(10, 20, 2)
    input = torch.randn(5, 3, 10)
    h0 = torch.randn(2, 3, 20)
    output, hn = rnn(input, h0)
    print()

def t2():
    data = torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    print("Data: ", data.shape, "\n\n", data)
    ###################### OUTPUT ######################


    # Number of features used as input. (Number of columns)
    INPUT_SIZE = 1
    # Number of previous time stamps taken into account.
    SEQ_LENGTH = 5
    # Number of features in last hidden state ie. number of output time-
    # steps to predict.See image below for more clarity.
    HIDDEN_SIZE = 2
    # Number of stacked rnn layers.
    NUM_LAYERS = 1
    # We have total of 20 rows in our input.
    # We divide the input into 4 batches where each batch has only 1
    # row. Each row corresponds to a sequence of length 5.
    BATCH_SIZE = 4

    # Initialize the RNN.
    rnn = nn.RNN(input_size=INPUT_SIZE, hidden_size=HIDDEN_SIZE, num_layers = 1, batch_first=True)
    # input size : (batch, seq_len, input_size)
    inputs = data.view(BATCH_SIZE, SEQ_LENGTH, INPUT_SIZE)
    # out shape = (batch, seq_len, num_directions * hidden_size)
    # h_n shape  = (num_layers * num_directions, batch, hidden_size)
    out, h_n = rnn(inputs)


if __name__ == '__main__':
    nn.Linear
    t1()
