
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision import transforms as T
import torch

training_dataset = datasets.FashionMNIST(root='./data', train=True, transform=T.ToTensor(), download=True)
test_dataset = datasets.FashionMNIST(root='./data', train=False, transform=T.ToTensor(), download=True)


print(training_dataset.classes)

training_loader = torch.utils.data.DataLoader(training_dataset, batch_size=4, shuffle=True, num_workers=0)
validation_loader = torch.utils.data.DataLoader(test_dataset, batch_size=4, shuffle=False, num_workers=0)

# next(iter(training_loader))

for i, data in enumerate(training_loader):
    batch_images, batch_labels = data
    break
