import timm
import torch
import torchvision
from PIL import Image
from torchvision import transforms as T
import json

if __name__ == '__main__':
    trans_ = T.Compose(
        [
         T.Resize(256),
         T.CenterCrop(224),
         T.ToTensor(),
         T.Normalize(timm.data.IMAGENET_DEFAULT_MEAN, timm.data.IMAGENET_DEFAULT_STD)]
    )

    image = Image.open('./house_finch.jpg')
    transformed = trans_(image)
    print(transformed.shape)
    batch_input = transformed.unsqueeze(0)
    print(batch_input.shape)

    model = timm.create_model('swin_base_patch4_window7_224', pretrained=True)

    with torch.no_grad():
        output = model(batch_input)

    print(output)
    print(output.shape)
    labels = json.load(open('./imagenet_labels.json'))
    class_ = output.argmax(dim=1)
    print(class_)
    print(class_.data)
    print(output.sum(dim=1))
    print(labels[class_])

