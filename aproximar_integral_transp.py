g = lambda x: (1. - x * x) ** (3. / 2.)

import random, math

nsim = 100000
integral = 0.
for i in range(0, nsim):
    x = random.random()  # U(0,1)
    gx = g(x)
    integral += gx

integral /= float(nsim)

error = abs(integral - 3. * math.pi / 6.)
print 'Integral= ', integral, '  error= ', error
s = 'Nsim=' + str(nsim) + '     I= ' + str(integral)
