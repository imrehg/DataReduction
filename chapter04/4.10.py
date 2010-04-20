#!/usr/bin/env python

from scipy import *
import scipy.integrate as integ
u = 100
s = 20

dist = lambda x, u, s:  1/(s * sqrt(2.0 * pi)) * exp(-(x - u)**2 / (2.0 * s**2))
vari = lambda x, u, s: x * x * dist(x, u, s)

p = (u, s)
s2 = 5
alist = linspace(8,9,200)
res = zeros(len(alist))
prob = zeros(len(alist))
for i, a in enumerate(alist):
    p = integ.quad(dist, u-a, u+a, args=(u, s))[0]
    v = sqrt(integ.quad(vari, u-a, u+a, args=(u, s))[0] / p - u*u)
    res[i] = v
    prob[i] = p
alim = alist[argmin(abs(res-5))]
ap = prob[argmin(abs(res-5))]
print "Approx. value of 'a': %f" %alim

n = 100000
np = 0
selected = []
import random
for k in xrange(n):
    resistance = random.normalvariate(u, s)
    if (u-alim) <= resistance <= (u+alim):
          selected.append(resistance)
print "==== Check by simulation ===="
print "Probability of selection: %f (expected: %f)" %(1.0 * len(selected) / n, ap)
print "Standard deviation %f" %(std(selected))
