##import numpy as np
##con numpy
# import random

# nsim=100000
# integral=0.
# for i in range(0,nsim):
##x=np.random.rand(8)
# x=random.random()
# gx=x.sum()**2
# integral+=gx

# integral*=2.**(-7)
# integral/=float(nsim)

# error=abs(integral-25./192.)
# print 'Integral= ', integral, '  error= ', error
# s='Nsim='+str(nsim)+'     I= '+ str(integral)

# sin numpy

print '\n SIN NUMPY'
import random
import math

nsim = 1000000
integral = 0.
# random.seed(3)
for i in range(0, nsim):
    x = []
    for k in range(0, 100):
        x.append(random.random())  # U(0,1)
    gx = sum(x) ** 2
    gx2 = math.exp(-gx)
    integral += gx2

# integral*=2.**(-7)
integral /= float(nsim)

# error=abs(integral-25./192.)
print 'Integral= ', integral  # , '  error= ', error
s = 'Nsim=' + str(nsim) + '     I= ' + str(integral)
