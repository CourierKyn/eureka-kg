"""This is a embedding processing."""

import torch
from torch import nn
from jieba import analyse

import numpy as np
import pandas as pd

_FEATURE_SIZE = 1


class _MixedInputModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(_MixedInputModel, self).__init__()
        self.embedding_dim = embedding_dim
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

    def forward(self, x):
        emb = self.embedding(x)
        emb = emb.view(1, -1)
        return emb


def _pretreatment(x):
    tf_idf = analyse.extract_tags
    series = x.fillna('unknown').apply(tf_idf)
    unique = set(series.sum())
    rep = dict(zip(unique, range(len(unique))))
    series = series.apply(lambda s: [rep[elem] for elem in s])
    return series.apply(np.mean)


def embedding(x):
    series = _pretreatment(x)
    model = _MixedInputModel(vocab_size=len(series), embedding_dim=_FEATURE_SIZE)
    x_input = torch.autograd.Variable(torch.LongTensor(list(series)))
    embed = model(x_input)
    # _FEATURE_SIZE == 2
    # embed = pd.DataFrame(embed.tolist(), index=range(1001, 4001, 1), columns=['x', 'y'])
    # datum_idx = torch.autograd.Variable(torch.LongTensor([0]))
    # datum_vector = model(datum_idx)
    # distance = _distance(embed, datum_vector)
    # return pd.Series(distance, name=x.name)

    # _FEATURE_SIZE == 1
    return pd.Series(embed.tolist()[0], name=x.name)
