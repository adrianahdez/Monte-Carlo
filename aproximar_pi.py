
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib
#from matplotlib.collections import PatchCollection
#import matplotlib.patches as mpatches

#fig = plt.figure(figsize=(5,5))
#ax = plt.subplot(111, aspect=1)


#art = mpatches.Rectangle((-1,-1),2,2,facecolor="white",ec='b',alpha=1,lw=1)

#ax.add_patch(art)

#art = mpatches.Circle((0.,0.), 1.,facecolor="y", ec="r", lw=2,alpha=0.25)

#ax.add_patch(art)


#ax.set_xticks([])
#ax.set_yticks([])
#ax.axis([-1.1,1.1,-1.1,1.1])
#ax.axis([0,1.05,0,1.05])

import random
nptos=0
ptosIn=0
nsim=100000000
#random.seed(10)
for i in range(0,nsim):
    #x=np.random.rand()
    #y=np.random.rand()
   x=random.random()
   y=random.random()
   nptos+=1
   if x**2+y**2<=1:
     ptosIn+=1
        #ax.plot([x],[y],'bx',lw=2,ms=5)
    #else:ax.plot([x],[y],'gx',lw=2,ms=5)

print 'ptosIn= ', ptosIn
vpi=4.*float(ptosIn)/float(nsim)
print 'pi= ', vpi
#s='Nsim='+str(nsim)+'     PI= '+ str(vpi)
#plt.title(s)
#plt.show()
