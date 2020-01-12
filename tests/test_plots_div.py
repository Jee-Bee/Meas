# -*- coding: utf-8 -*-
"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# x = np.linspace(0, 10)
# line, = plt.plot(t, sig, '--', linewidth=2)
# line, = plt.plot(x, '--', linewidth=2)
#
# dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
# line.set_dashes(dashes)
#
# plt.show()

#
# ----------------------------- New Test -------------------------------------
#

import numpy as np
import matplotlib.pyplot as plt

fs = 512
t = np.arange(0.0, 2.0, 1 / fs)
s = np.sin(250 * np.pi * t)

plt.figure()
plt.plot(t, s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
# plt.savefig("test.png")
plt.show()

# --------------------------------------------------------------
# 3d print script test
# Method 1:
# http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html


from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(4)
y = np.arange(-len(x)/2, len(x)/2)
z = np.random.rand(len(x), len(x))
z = np.round(z, decimals=2)

x, y = np.meshgrid(x, y)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection="3d")  # breaks option for colorbar
# ax1 = fig1.gca(projection='3d')
# ax1.plot_surface(x, y, z, cmap="autumn_r", lw=0.5, rstride=1, cstride=1)
ax1.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm)  # ,
#                       linewidth=0, antialiased=False)
ax1.set_zlim(-0.01, 1.01)
ax1.azim = -90
ax1.elev = 90

# ax1.zaxis.set_major_locator(LinearLocator(10))
# ax1.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# fig1.colorbar(ax1, shrink=0.5, aspect=5)

fig1.show()

# Method 2:
# http://matplotlib.org/examples/pylab_examples/colorbar_tick_labelling_demo.html
# http://stackoverflow.com/questions/2643953/attributeerror-while-adding-colorbar-in-matplotlib#2644255

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

#x = np.arange(4)
#y = np.arange(-len(x)/2, len(x)/2)
#z = np.random.rand(len(x), len(x))
#z = np.round(z, decimals=2)

fig2, ax2 = plt.subplots()  # plt.figure()

cax = ax2.imshow(z, interpolation='nearest', cmap=cm.coolwarm)
ax2.set_title = "implot rand vals"

# tickvals = np.linspace(np.amin(z), np.amax(z), 3)
cbar = fig2.colorbar(cax, ticks=[-1,0,1])# tickvals)
# http://stackoverflow.com/questions/5365520/numpy-converting-array-from-float-to-strings
# ytlabels = ['< -1', '0', '> 1']
ytlabels = np.array(tickvals).reshape(-1,)
ytlabels = list(ytlabels)
# ytlabels = ytlabels.astype('|S10')
ytlabels[0] = 'Min'; ytlabels[-1] = 'Max'
cbar.ax2.set_yticklabels(ytlabels)  # vertically oriented colorbar

fig2.show()
