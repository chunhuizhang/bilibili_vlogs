from transformers import BertModel, BertTokenizer
from transformers.models.bert import BertModel
import torch
from torch import nn

nn.BatchNorm2d()

if __name__ == '__main__':

    model_name = 'bert-base-uncased'

    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name, output_hidden_states=True)

    text = "After stealing money from the bank vault, the bank robber was seen " \
       "fishing on the Mississippi river bank."

    model.eval()
    token_inputs = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**token_inputs)





