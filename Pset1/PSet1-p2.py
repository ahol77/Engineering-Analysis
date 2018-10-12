import numpy as np
import matplotlib as mp
import scipy
from matplotlib import pyplot as plt

t1 = np.linspace(0,10,1000)
t2 = np.linspace(10,20,1000)
c1 = .5-.5 * np.exp(-t1/50)
c2 = .1107 * np.exp(-t2/50)

plt.close('all')

plt.plot(t1, c1,'b')
plt.plot(t2, c2,'b')
plt.xlabel('Time (min)', fontsize=14, fontstyle='italic')
plt.ylabel('Concentration (kg/L)', fontsize=14, fontstyle='italic')
plt.title("Concentration of Tank vs Time",fontsize=18)

plt.savefig('concoftank.png')

plt.show()