import torch
from torch import nn
from d2l import torch as d2l

class LongTermAttentionBasedPoolingLayer(nn.Module):
    def __init__(self,**kwargs):
        super(LongTermAttentionBasedPoolingLayer, self).__init__(kwargs)

class LongAndShortTermAttentionBasedPoolingLayer(nn.Module):
    def __init__(self,**kwargs):
        super(LongAndShortTermAttentionBasedPoolingLayer, self).__init__(kwargs)


d2l.MultiHeadAttention()

class SHAN_model(nn.Module):
    def __init__(self,**kwargs):
        super(SHAN_model,self).__init__(kwargs)
    def forward(self,X):
