# -*- coding: utf-8 -*-


import numpy as np
import math

def length(vector):
    return np.linalg.norm(vector)

def normalize(vector):
    if type(vector) == list:
        vector = np.array(vector)
    norm = np.linalg.norm(vector)
    return vector / norm

def dot(v1, v2):
    return np.dot(v1, v2)

def cross(v1, v2):
    v1x = v1[0]
    v1y = v1[1]
    v1z = v1[2]
    v2x = v2[0]
    v2y = v2[1]
    v2z = v2[2]
    lst = [(v1y * v2z) - (v1z * v2y), (v1z * v2x) - (v1x * v2z), (v1x * v2y) - (v1y * v2x)]
    return np.array(lst,dtype=np.float32)

