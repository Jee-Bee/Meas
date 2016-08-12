# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:43:07 2016

@author: enjbwink
"""

import numpy.random as rand
import matplotlib.pylab as plt

rbin = rand.binomial(1,1,1024)
rexp = rand.exponential(1,1024)
rnor = rand.normal(1,1,1024)
rpow = rand.power(1,1024)
rran = rand.rand(1,1024)
runi = rand.uniform(0,1,1024)

plt.figure()
plt.subplot(2,3,1), plt.hist(rbin), plt.title('Binominaal')
plt.subplot(2,3,2), plt.hist(rexp), plt.title('Exponential')
plt.subplot(2,3,3), plt.hist(rnor), plt.title('Normal')
plt.subplot(2,3,4), plt.hist(rpow), plt.title('Power')
plt.subplot(2,3,5), plt.hist(rran), plt.title('Rand')
plt.subplot(2,3,6), plt.hist(runi), plt.title('Uniform')