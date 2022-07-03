
from transformers import BertModel, BertTokenizer

model_name = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

raw_sentences = ['Tom likes cats', 'Liz likes dogs']

inputs = tokenizer.encode_plus(raw_sentences[0], raw_sentences[1], return_tensors='pt')
# inputs = tokenizer('Hello, my dog is cute', return_tensors='pt')
model(**inputs)
