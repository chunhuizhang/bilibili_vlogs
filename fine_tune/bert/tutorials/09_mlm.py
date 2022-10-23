
import torch
from transformers.models.bert import BertModel, BertTokenizer, BertForMaskedLM


model_type = 'bert-base-uncased'

tokenizer = BertTokenizer.from_pretrained(model_type)
bert = BertModel.from_pretrained(model_type)
mlm = BertForMaskedLM.from_pretrained(model_type, output_hidden_states=True)


text = ("After Abraham Lincoln won the November 1860 presidential "
        "election on an anti-slavery platform, an initial seven "
        "slave states declared their secession from the country "
        "to form the Confederacy. War broke out in April 1861 "
        "when secessionist forces attacked Fort Sumter in South "
        "Carolina, just over a month after Lincoln's "
        "inauguration.")

inputs = tokenizer(text, return_tensors='pt')
inputs['labels'] = inputs['input_ids'].detach().clone()

mask_arr = (torch.rand(inputs['input_ids'].shape) < 0.15) \
        * (inputs['input_ids'] != 101) \
        * (inputs['input_ids'] != 102)
selection = torch.flatten(mask_arr[0].nonzero()).tolist()
inputs['input_ids'][0, selection] = 103

mlm.eval()
with torch.no_grad():
    output = mlm(**inputs)
print()