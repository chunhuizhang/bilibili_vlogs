import random
import torch
from cv.image_similarity.cnn.build_models import IR_50, IR_101, IR_152
import torchvision
import os
from PIL import Image


to_torch_tensor = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
                                  torchvision.transforms.Normalize([0.5, 0.5, 0.5],[0.5, 0.5, 0.5])])



def l2_norm(input, axis=1):
    norm = torch.norm(input, 2, axis, True)
    output = torch.div(input, norm)

    return output


def init_model(model, param, device):
    m = model([112, 112])
    m.eval()
    m.to(device)
    m.load_state_dict(torch.load(param, map_location=torch.device('cpu')))
    return m


def get_model_pool(device):
    model_pool = []
    # double
    model_pool.append(init_model(IR_50, 'models/backbone_ir50_ms1m_epoch120.pth', device))
    # model_pool.append(init_model(IR_50, 'models/backbone_ir50_ms1m_epoch120.pth', device))
    #
    # model_pool.append(init_model(IR_50, 'models/Backbone_IR_50_LFW.pth', device))
    # model_pool.append(init_model(IR_101, 'models/Backbone_IR_101_Batch_108320.pth', device))
    # model_pool.append(init_model(IR_152, 'models/Backbone_IR_152_MS1M_Epoch_112.pth', device))
    return model_pool


def get_model(device):
    return init_model(IR_50, 'models/backbone_ir50_ms1m_epoch120.pth', device)


device = torch.device('cpu')
model = get_model(device)
print('----models load over----')
images = os.listdir('../imgs/lena')


vectors = []

for img in images:
    print(img)
    img = Image.open('../imgs/lena/' + img).convert('RGB')
    # print(dir(img))
    print(img.size, img.mode)
    img = to_torch_tensor(img.resize((112, 112), Image.ANTIALIAS))
    img = img.unsqueeze_(0).to(device)
    feature = model(img)
    vectors.append(l2_norm(feature).detach_())

print('----vectors calculate over----')


for i in range(len(vectors)):
    for j in range(len(vectors)):
        # consine distance
        dist = (vectors[i]*vectors[j]).sum().item()
        print(images[i], images[j], dist)
    print('-------------')
