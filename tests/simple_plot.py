import matplotlib.pylab as plt
#from pylab import *


t = plt.arange(0.0, 2.0, 0.01)
s = plt.sin(2*plt.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
