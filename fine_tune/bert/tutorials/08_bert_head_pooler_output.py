
from transformers.models.bert import BertTokenizer, BertModel, BertForMaskedLM
import torch

model_type = 'bert-base-uncased'
text = 'This is a text sentence.'

bert = BertModel.from_pretrained(model_type)
tokenizer = BertTokenizer.from_pretrained(model_type)

inputs = tokenizer(text, return_tensors='pt')
