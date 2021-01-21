# -*- coding: utf-8 -*-

import numpy as np
import math


PI = 3.1415926535

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
    
    @property
    def func(self):
        return self.__func
    
    def integrate(self):
        return self.__funcInt
    
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
            
        marginalFunc = []
        for v in range(0, nv):
            marginalFunc.append(self.__pConditionalV[v].integrate())
        self.__pMarginal = Distribution1D(np.array(marginalFunc, np.float32), nv)
        
    def sample_continuous(self, u):
        '''u ∈ [0,1]^2'''
        d1, pdf1, v = self.__pMarginal.sample_continuous(u[1])
        d0, pdf0, u = self.__pConditionalV[v].sample_continuous(u[0])
        pdf = pdf1 * pdf0
        return d0, d1, pdf
    
    def pdf(self, p):
        '''p ∈ [0,1]^2'''
        iu = clamp(int(p[0] * self.__pConditionalV[0].count()), 0, self.__pConditionalV[0].count() - 1)
        iv = clamp(int(p[1] * self.__pMarginal.count()), 0, self.__pMarginal.count() - 1)
        return self.__pConditionalV[iv].func[iu] / self.__pMarginal.integrate()

def square_to_disk(u):
    r = sqrt(u[0])
    theta = Pi * u[1]
    return (r * math.cos(theta), r * math.sin(theta))



arr = np.random.randint(1, 20, (10, 10))

s = arr.sum()

arr = arr.astype(np.float32) / s

d2d = Distribution2D(arr)

# print(arr[9][9] /)
print(d2d.pdf([0.81,0.81]))
print(d2d.pdf([0.96,0.96]))