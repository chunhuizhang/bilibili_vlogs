
import torch
from transformers.models.bert import BertModel, BertTokenizer


if __name__ == '__main__':
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name, output_hidden_states=True)

    test_sent = 'this is a test sentence'

    model_input = tokenizer(test_sent, return_tensors='pt')
    model.eval()
    with torch.no_grad():
        output = model(**model_input)

