
import transformers
from transformers import pipeline
import torch.nn.functional as F
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
# model_name = 'bert-base-uncased'

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# clf = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
#
# test_sentence = 'today is not that bad'
test_sentences = ['today is not that bad', 'today is so bad']
# res = clf(test_sentences)
# print(res)
#


batch = tokenizer(test_sentences, padding='max_length', truncation=True, max_length=512, return_tensors='pt')

with torch.no_grad():
    # print(**batch)
    outputs = model(**batch)
    print(outputs)
    scores = F.softmax(outputs.logits, dim=1)
    labels = torch.argmax(scores, dim=1)
    labels = [model.config.id2label[id] for id in labels.tolist()]
    print(labels)
