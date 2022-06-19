
import torch
from datasets import load_dataset
from transformers import BertTokenizer


#定义数据集
class Dataset(torch.utils.data.Dataset):
    def __init__(self, split):
        dataset = load_dataset(path='seamew/ChnSentiCorp', split=split)

        def f(data):
            return len(data['text']) > 30

        self.dataset = dataset.filter(f)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, i):
        text = self.dataset[i]['text']

        return text

if __name__ == '__main__':
    dataset = Dataset('train')
    print(len(dataset), dataset[0])
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
