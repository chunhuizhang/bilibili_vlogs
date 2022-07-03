
from transformers import BertModel, BertForSequenceClassification
from collections import defaultdict
import matplotlib.pyplot as plt


model_name = 'bert-base-uncased'

model = BertModel.from_pretrained(model_name)
cls_model = BertForSequenceClassification.from_pretrained(model_name)



total_params = 0
total_learnable_params = 0
total_embedding_params = 0
total_encoder_params = 0
total_pooler_params = 0

params_dict = defaultdict(float)

for name, para in model.named_parameters():
    print(name, para.shape, para.numel())
    if para.requires_grad:
        total_learnable_params += para.numel()
    total_params += para.numel()
    if 'embedding' in name:
        params_dict['embedding'] += para.numel()
        total_embedding_params += para.numel()
    if 'encoder' in name:
        layer_index = name.split('.')[2]
        params_dict['encoder({})'.format(layer_index)] += para.numel()
        total_encoder_params += para.numel()
    if 'pooler' in name:
        params_dict['pooler'] += para.numel()
        total_pooler_params += para.numel()


print(total_params)
print(total_learnable_params)
print(params_dict)
print(total_embedding_params)
print(total_encoder_params)
print(total_pooler_params)