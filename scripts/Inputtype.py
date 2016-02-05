# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:45:23 2016

@author: enjbwink
"""

# scale type(float int etc)
# 
# scale based on size <1 en >1.
# scale to 1 and then times signal

# 2 Do
# Fix error messages 

import numpy




def input_type (data):
    if numpy.ndim(data) > 0:
        if isinstance(data[0],numpy.float):
            return (data)
        elif isinstance(data[0],numpy.int64):
            data = data.astype(float)/(2**(64-1))
            return (data)
        elif isinstance(data[0],numpy.int32):
            data = data.astype(float)/(2**(32-1))
            return (data)
        elif isinstance(data[0],numpy.int16):
            data = data.astype(float)/(2**(16-1))
            return (data)
        elif isinstance(data[0],numpy.int8):
            data = data.astype(float)/(2**(8-1))
            return (data)
        else:
            print('wrong input type')
    elif numpy.ndim(data) == 0:
        if isinstance(data,numpy.float):
            return (data)
        elif isinstance(data,numpy.int64):
            data = data.astype(float)/(2**(64-1))
            return (data)
        elif isinstance(data,numpy.int32):
            data = data.astype(float)/(2**(32-1))
            return (data)
        elif isinstance(data,numpy.int16):
            data = data.astype(float)/(2**(16-1))
            return (data)
        elif isinstance(data,numpy.int8):
            data = data.astype(float)/(2**(8-1))
            return (data)
        else:
            print('wrong input type') 

def input_check (data):
    if numpy.ndim(data) > 0:
        if isinstance(data[0],numpy.float):
            return (True)
        else:
            print('wrong input type')
            return (False)
    elif numpy.ndim(data) == 0:
        if isinstance(data,numpy.float):
            return (True)
        else:
            return (False)
            print('wrong input type')
