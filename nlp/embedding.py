"""This is a embedding processing."""
import torch
from torch import nn
import pandas as pd

_ROW_SIZE = 3000
_FEATURE_SIZE = 1


class _MixedInputModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(_MixedInputModel, self).__init__()
        self.embedding_dim = embedding_dim
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, x):
        emb = self.embedding(x)
        emb = emb.view(1, -1)  # change to one row
        return emb


def _text_processing(x, word_to_ix):
    x = x.replace(word_to_ix).astype('float')
    return x


def embedding(x, word_to_ix):
    x = _text_processing(x, word_to_ix)
    model = _MixedInputModel(vocab_size=_ROW_SIZE, embedding_dim=_FEATURE_SIZE)
    x_input = torch.autograd.Variable(torch.LongTensor(list(x)))
    embed = model(x_input)
    return pd.Series(embed[0].detach().numpy())


# example
series = pd.Series(['hello', 'world'])
replace_dict = {'hello': 0, 'world': 1}
