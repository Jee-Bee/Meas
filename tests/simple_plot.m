# simple plot for test equality with python

T = 2;
fs = 512;
t = 0:1/fs:T-1/fs;
s = sin(250 * pi * t);

plot(t,s)
xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
%grid(On)