from torchvision import transforms
import torchvision
import torch


# global, whole training dataset
# x' = (x-mean)/std
# x'*std + mean => x

# timm.data.IMAGENET_DEFAULT_MEAN: (0.485, 0.456, 0.406)
# timm.data.IMAGENET_DEFAULT_STD: (0.229, 0.224, 0.225)
transform = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.1307],  std=[0.3081]),
                # transforms.Resize()
            ])

# MNIST dataset
mnist = torchvision.datasets.MNIST(root='./data/',
                                   train=True,
                                   transform=transform,
                                   download=True)
batch_size = 32
# Data loader
data_loader = torch.utils.data.DataLoader(dataset=mnist,
                                          batch_size=batch_size,
                                          shuffle=True)

epochs = 10

for epoch in range(epochs):

    for i, (images, t) in enumerate(data_loader):
        print(images)