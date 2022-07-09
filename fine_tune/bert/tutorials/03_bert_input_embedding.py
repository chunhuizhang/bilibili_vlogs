
from transformers import BertTokenizer, BertModel
from transformers.models.bert import BertModel
import torch
from torch import nn


model_name = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name, output_hidden_states=True)

test_sent = 'this is a test sentence'

model_input = tokenizer(test_sent, return_tensors='pt')


model.eval()
with torch.no_grad():
    output = model(**model_input)