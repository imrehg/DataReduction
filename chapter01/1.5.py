#!/usr/bin/env python

from numpy import *
filename = '1.5.txt'
data = loadtxt(filename)
y = sorted(data[:,1])

print "Mean: %f" %mean(y)
print "Median %d" %y[int(len(y) / 2.0)]
groups = 10
mprob = [0]*(max(y) / groups)
# Use the "different" integer division in python: 6 / 5 = 1
for roll in y:
    mprob[int(roll)/groups -1] += 1
mostprob = argmax(mprob)
rmin = mostprob * groups
rmax = rmin + groups - 1
print "Most probable region: %d - %d (%d occurence)" %(rmin, rmax, mprob[mostprob])
print "Sample standard deviation: %f" %sqrt(sum(power(y - mean(y), 2))/(len(y)-1))
