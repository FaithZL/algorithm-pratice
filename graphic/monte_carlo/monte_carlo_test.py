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

def Clamp(a, l, h):
    if a < l:
        return l
    if a > h:
        return h
    return a

B = 1

N = 10

A = B * B

o = np.array([0,0,0], np.float32)

# plane
z = 1.0

p0 = np.array([0,0,z], np.float32)
p1 = np.array([B,0,z], np.float32)
p2 = np.array([0,B,z], np.float32)
p3 = np.array([B,B,z], np.float32)

arr = np.random.randint(1,20,size=(N,N))

arr = np.ones(shape=(N,N))

PI = 3.1415926535

pdfArr = arr.astype(np.float32) / arr.sum()

integrate = 0

def solidAngle(p, p0,p1,p2):
    v0 = normalize(p0 - p)
    v1 = normalize(p1 - p)
    v2 = normalize(p2 - p)

    c01 = cross(v0, v1)
    c12 = cross(v1, v2)
    c20 = cross(v2, v0)
    if length(c01) > 0:
        c01 = normalize(c01)
    if length(c12) > 0:
        c12 = normalize(c12)
    if length(c20) > 0:
        c20 = normalize(c20)
    
    ret = math.acos(Clamp(dot(c01, -c12), -1, 1)) + math.acos(Clamp(dot(c12, -c20), -1, 1)) + math.acos(Clamp(dot(c20, -c01), -1, 1)) - PI
    return abs(ret)

for X in range(0, N):
    x = X / N * B
    for Y in range(0, N):
        y = Y / N * B
        vec = np.array([x, y, 1], np.float32)
        l = length(vec)
        cosTheta = z / l
        pdfA = pdfArr[X][Y]
        pdfW = ((l * l) / cosTheta) * pdfA
        
        # print(pdfArr[X][Y])
        # integrate += pdfA
        integrate += pdfW

s1 = solidAngle(o, p0, p1, p3)
s2 = solidAngle(o, p0, p2, p3)

print(s1 + s2)
print(integrate)