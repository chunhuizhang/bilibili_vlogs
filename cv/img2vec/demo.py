import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable
from PIL import Image
import os
from torchvision import transforms as T


# Load the pretrained model
model = models.resnet152(pretrained=True)

layer = model._modules['avgpool']
# Set model to evaluation mode
model.eval()


# scaler = transforms.Scale((224, 224))
# normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                                  std=[0.229, 0.224, 0.225])
# to_tensor = transforms.ToTensor()

trans = T.Compose([
    # T.Resize(256),
    # T.CenterCrop(224),
    T.Scale((256, 256)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

def get_vector(image_name):
    # 1. Load the image with Pillow library
    img = Image.open(image_name)
    # 2. Create a PyTorch Variable with the transformed image
    t_img = trans(img).unsqueeze(0)
    # 3. Create a vector of zeros that will hold our feature vector
    #    The 'avgpool' layer has an output size of 512
    my_embedding = torch.zeros(2048)
    # # 4. Define a function that will copy the output of a layer
    def copy_data(m, i, o):
        my_embedding.copy_(o.data.reshape(o.data.size(1)))
    # 5. Attach that function to our selected layer
    h = layer.register_forward_hook(copy_data)
    # # 6. Run the model on our transformed image
    model(t_img)
    # # 7. Detach our copy function from the layer
    h.remove()
    # 8. Return the feature vector
    return my_embedding


if __name__ == '__main__':
    imgs = []
    img_vecs = []
    for img_file in os.listdir('./imgs'):
        imgs.append(img_file)
        img_file = os.path.join('./imgs', img_file)
        vec = get_vector(img_file)
        img_vecs.append(vec)
        print(vec.shape, type(vec))

    cos = nn.CosineSimilarity(dim=1)

    for i in range(0, len(imgs)):
        for j in range(i, len(imgs)):
            print(imgs[i], imgs[j], cos(img_vecs[i].unsqueeze(0), img_vecs[j].unsqueeze(0)))


