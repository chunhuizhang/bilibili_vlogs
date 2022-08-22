from bertviz.transformers_neuron_view import BertModel, BertConfig
from transformers import BertTokenizer
import torch
import math

import numpy as np

np.random.seed(1234)

max_length = 256
config = BertConfig.from_pretrained("bert-base-uncased", output_attentions=True, output_hidden_states=True, return_dict=True)
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
config.max_position_embeddings = max_length



from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train')
inputs_tests = tokenizer(newsgroups_train['data'][:1],
                         truncation=True,
                         padding=True,
                         max_length=max_length,
                         return_tensors='pt')
# print(inputs_tests['input_ids'])
# with torch.no_grad():
#     model = BertModel(config)
#     # print(config)
#     embed_output = model.embeddings(inputs_tests['input_ids'], inputs_tests['token_type_ids'], )
#     model_output = model(**inputs_tests)
#     print(embed_output)
#     print(model_output[-1][0]['attn'][0, 0, :, :])

# print(inputs_tests['input_ids'])
with torch.no_grad():
    model = BertModel(config)
    # print(config)
    embed_output = model.embeddings(inputs_tests['input_ids'], inputs_tests['token_type_ids'], )
    print(embed_output)
    model_output = model(**inputs_tests)
    print(model_output[-1][0]['attn'][0, 0, :, :])
    att_head_size = int(model.config.hidden_size/model.config.num_attention_heads)
    Q_first_head = embed_output[0] @ model.encoder.layer[0].attention.self.query.weight.T[:, :att_head_size] + \
                   model.encoder.layer[0].attention.self.query.bias[:att_head_size]
    K_first_head = embed_output[0] @ model.encoder.layer[0].attention.self.key.weight.T[:, :att_head_size] + \
                   model.encoder.layer[0].attention.self.key.bias[:att_head_size]
    # mod_attention = (1.0 - inputs_tests['attention_mask'][[0]]) * -10000.0
    attention_scores = torch.nn.Softmax(dim=-1)((Q_first_head @ K_first_head.T)/ math.sqrt(att_head_size))
    print(attention_scores)

