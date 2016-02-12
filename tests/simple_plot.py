import matplotlib.pylab as plt
#from pylab import *

fs = 512
t = plt.arange(0.0, 2.0, 1/fs)
s = plt.sin(250*plt.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
