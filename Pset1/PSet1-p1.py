import numpy as np
import matplotlib as mp
from scipy import integrate
from matplotlib import pyplot as plt

def snw_fll(t):
    return ((4+3*np.cos(2*np.pi*t/365))*200/1000)
def snw_mlt(t):
    return ((12-10*np.cos(2*np.pi*t/365))*86400/334/1000)
def mass(t):
    return (-2.3044*t + 3.187*365/(2*np.pi)*np.sin(2*np.pi*t/365))
a = integrate.quad(snw_fll,0,320.701)
b = integrate.quad(snw_mlt,0,320.701)
c = a[0] - b[0]
print(c)

t = np.linspace(0,365,1000)

plt.close('all')

plt.plot(t, mass(t),"r-", linewidth=3)
plt.xlabel('Time (days)', fontsize=14, fontstyle='italic')
plt.ylabel('Mass per Area (kg/m^2)', fontsize=14, fontstyle='italic')
plt.title("Mass of Glacier During One Year",fontsize=18)

plt.arrow(44,-200,0,180,head_width=15,width=3,facecolor='k')
plt.annotate("Maximum Mass", xy=(44, -250),horizontalalignment="center")

plt.arrow(320,-620,0,-200,head_width=15,width=3,facecolor='k')
plt.annotate("Minimum Mass", xy=(320, -570),horizontalalignment="center")

plt.savefig('glaciermass.png')

plt.show()
