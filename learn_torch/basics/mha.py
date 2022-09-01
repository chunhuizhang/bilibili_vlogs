import torch
from torch import nn

if __name__ == '__main__':

    mha = nn.MultiheadAttention(embed_dim=768, num_heads=12, kdim=10, vdim=20)

    query = torch.randn(10, 1, 768)
    key = torch.randn(5, 1, 10)
    value = torch.randn(5, 1, 20)

    attn_output, attn_output_weights = mha(query, key, value)
    print(attn_output.shape)
    print(attn_output_weights.shape)


