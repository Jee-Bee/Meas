# -*- coding: utf-8 -*-
"""
Demo of a simple plot with a custom dashed line.

A Line object's ``set_dashes`` method allows you to specify dashes with
a series of on/off lengths (in points).
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
line, = plt.plot(t, sig, '--', linewidth=2)

dashes = [10, 5, 100, 5]  # 10 points on, 5 off, 100 on, 5 off
line.set_dashes(dashes)

plt.show()

#
# ----------------------------- New Test -------------------------------------
#

fs = 512
t = plt.arange(0.0, 2.0, 1/fs)
s = plt.sin(250*plt.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
# plt.savefig("test.png")
plt.show()