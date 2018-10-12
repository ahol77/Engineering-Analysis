import numpy as np
from matplotlib import pyplot as plt
#Cats Speed
a=20
#Dogs Distance from y axis
c=150

#Function solving for distance the cat can be away from the tree
def distance(b):
    return c*(a*b)/((b**2)-(a**2))

#Create array of speeds dog could have
b=np.linspace(0,30,100)

plt.close('all')

plt.plot(b, distance(b),'b')
plt.xlabel("Dog's Speed (ft/s)", fontsize=14, fontstyle='italic')
plt.ylabel("Cat's Distance from Tree (ft", fontsize=14, fontstyle='italic')
plt.title("Distance Cat can Safely be from Tree to Escape Dog",fontsize=18)

plt.savefig('dogchasecat.png')

plt.show()


