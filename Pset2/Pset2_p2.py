import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
from numpy import random as rng

pts = 10000

t = np.linspace(-1, 1.2, pts)
R1 = 2*rng.randn(pts)
R2 = 2*rng.randn(pts)

x = t**3 + 0.6*R1
y = t**6 + 0.3*R2

mean = np.mean(R1)
std = np.std(R1)

print("Mean:", mean)
print("STD:", std)

plt.close('all')

fig1 = plt.figure()
plt.plot(x,y, 'o', markersize=2)
plt.xlabel('x(t)', fontsize=14, fontstyle='italic')
plt.ylabel('y(t)', fontsize=14, fontstyle='italic')
plt.title("y(t) vs x(t)",fontsize=18)
plt.savefig('scatterplot1')

fig2 = plt.figure()
plt.subplot(121)
counts,xbins,ybins,image = plt.hist2d(x,y,bins=25
                                      ,norm=LogNorm()
                                      , cmap = plt.cm.rainbow)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Histogram of Point Density",fontsize=12)
plt.subplot(122)
plt.contour(counts.transpose(),extent=[xbins[0],xbins[-1],ybins[0],ybins[-1]],
    linewidths=3, cmap = plt.cm.rainbow, levels = [1,5,10,25,50,70,80,100])
plt.xlabel('x')
plt.ylabel('y')
plt.title("Contour Map of Point Density",fontsize=12)
cbar = plt.colorbar()
cbar.ax.set_ylabel('Counts')
plt.subplots_adjust(wspace=.5)
plt.savefig('contourmap')