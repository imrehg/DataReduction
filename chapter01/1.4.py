#!/usr/bin/env python

from numpy import *
filename = '1.4.txt'
data = loadtxt(filename)
y = sorted(data[:,1])

print "Mean: %f" %mean(y)
print "Median %d" %y[int(len(y) / 2.0)]
mprob = [0]*max(y)
for roll in y:
    mprob[int(roll)-1] += 1
mostprob = argmax(mprob)
print "Most probable value: %d (%d occurence)" %(mostprob, mprob[mostprob])
print "Sample standard deviation: %f" %sqrt(sum(power(y - mean(y), 2))/(len(y)-1))
