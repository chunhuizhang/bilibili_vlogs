import torch


def and_gate():
    and_weights = torch.tensor([1, 1, -2])
    

if __name__ == '__main__':
    # x1, x2, b
    X = torch.tensor([(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 1)], dtype=torch.double)

    print(X)
    pass
