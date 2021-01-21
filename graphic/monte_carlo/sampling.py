# -*- coding: utf-8 -*-

import numpy as np
import math

def clamp(a, l, h):
    if a < l:
        return l
    if a > h:
        return h
    return a

def find_interval(size, pred):
    first = 0
    length = size
    while length > 0:
        half = length >> 1
        middle = first + half
        if pred(middle):
            first = middle + 1
            length = length - (half + 1)
        else:
            length = half
    return clamp(first - 1, 0, size - 2)

class Distribution1D(object):
    def __init__(self, func, n):
        self.__func = func
        
        self.__cdf = None
        
        self.__funcInt = 0
        
        self.update_cdf(self.__func, n)
        
    def update_cdf(self, func, n):
        cdf = np.zeros((len(func) + 1), dtype=np.float32)
        cdf[0] = 0
        for i in range(1, n + 1):
            cdf[i] = cdf[i - 1] + func[i - 1] / n
            
        funcInt = cdf[n]
        
        if self.__funcInt == 0:
            for i in range(1, n + 1):
                cdf[i] = i / n
        else:
            for i in range(1, n + 1):
                cdf[i] = cdf[i] / funcInt
                
        self.__funcInt = funcInt
        self.__cdf = cdf
        
    def count(self):
        return len(self.__func)
    
    def sample_continuous(self, u):
        
        def pred(index):
            return self.__cdf[index] <= u
        
        offset = find_interval(len(self.__cdf), pred)
        
        du = u - self.__cdf[offset]
        
        if (self.__cdf[offset + 1] - self.__cdf[offset]) > 0:
            du = du / (self.__cdf[offset + 1] - self.__cdf[offset])

        pdf = self.__func[offset] / self.__funcInt if self.__funcInt > 0 else 0
        
        return (offset + du) / self.count(), pdf, offset
    
    def sample_discrete(self, u):
        def pred(index):
            return self.__cdf[index] <= u
        
        offset = find_interval(len(self.__cdf), pred)
        pdf = self.__func[offset] / (self.__funcInt * self.count()) if self.__funcInt > 0 else 0
        
        uRemapping = (u - self.__cdf[offset]) / (self.__cdf[offset + 1] + self.__cdf[offset])

        return offset, pdf, uRemapping
    
    def discrete_pdf(self, index):
        return self.__func[index] / (self.__funcInt * self.count())
    
    
class Distribution2D(object):
    
    def __init__(self, data):
        nv, nu = data.shape
        
        self.__pConditionalV = []

        for v in range(0, nv):
            d1d = Distribution1D(data[v], nu)
            self.__pConditionalV.append(d1d)
        

# a = np.ones((2,3))
# print(a)