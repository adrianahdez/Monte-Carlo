import random

r1Points = 0
r2Points = 0
r3Points = 0
nsim = 10000

random.seed(1)

for i in range(0, nsim):
    x = random.random()
    y = random.random()

    if x ** 2 + y ** 2 <= 1:
        r1Points += 1
        if -.6 <= x <= .6:
            r2Points += 1
            if x ** 2 + y ** 2 >= .5 ** 2:
                r3Points += 1

r1 = 4. * float(r1Points) / float(nsim)
r2 = 4. * float(r2Points) / float(nsim)
r3 = 4. * float(r3Points) / float(nsim)

print('R1 Area = ', r1, '\nR2 Area = ', r2, '\nR3 Area = ', r3)
