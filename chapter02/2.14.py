
import numpy.random as nrand
from numpy import exp, array
from pylab import *


# Detector efficiency
countereff = lambda u: (1 - exp(-u))/u

# Rates
rate = array([1e6, 2e6, 4e6, 6e6, 8e6, 10e6])
deadtime = 200e-9
# Expected number of clicks during the deadtime
u = deadtime * rate[0]

# Numerical simulation
n = 100000
x = nrand.poisson(lam = u, size=n)
y = 1.0 * sum([1 for a in x if a > 0]) / n
print "=== Simulation test (%d repeats) ===" %n
print "Efficiency at (u = %f) : %f" %(u, y / u)
print "Expected efficiency    : %f" %countereff(u)

# Plot the different rates
uall = deadtime * rate 
plot(rate/1e6,  map(countereff, uall))
xlabel("Rate (1e6/s)")
ylabel("Detector fficiency")
show()
