# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:50:14 2016

@author: Jee-Bee for jBae (c) 2016
"""
import numpy as np
# from numpy import append

# a = []
# for idx in range(2):
#     for idy in range(5):
#         print(idx, idy)
#         a.append(np.array([idx, idy]))

b = np.array([[1, 2], [2, 3], [0, 1], [0, 0], [3, 1], [2, 0]])
print(b)

(rows, cols) = np.shape(b)
delrows = []
for idx in range(rows):
    for idy in range(cols):
        if b[idx][idy] == 0:
            if len(delrows) == 0:
                delrows.append(idx)
                print(idx, idy)
            elif delrows[-1] == idx:
                pass 
            else:
                delrows.append(idx)
                print(idx, idy)
        else:
            pass
print(delrows)
b = np.delete(b, delrows, 0)
print(b)
# http://mednis.info/wp/?p=340
# idx = 0
# idy = 0
# while idx < rows:
#     while idy < cols:
#         if b[idx][idy] == 0:
#             np.delete(b, s_[idx], axis=0) # remove rows 1 and 2
#             (rows,cols) = np.shape(b)
#             print(idx, idy)
#         else:
#             pass
#         idy +=1
#         print (idy)
#     idx += 1
#     print (idx)
#     idy=0

# def indices(a, func):
#     (rows,cols) = np.shape(a)
#     for idxc in range(cols):
#        
#     return [i for (i,val) in enumerate(a) if func(val)]


# def indices(a, func):
#     (rows,cols) = np.shape(a)
#     for idxc in range(cols):
#        
#     return [i for (i,val) in enumerate(a) if func(val)]
#
# cs = abs(peak/rms)
#
# inds = indices(cs,lambda x: x == 0)
