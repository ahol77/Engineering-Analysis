import numpy as np
import matplotlib as mp
import scipy
from matplotlib import pyplot as plt

v_o = 0.0
def rate(v_o, t):
    g=9.81
    m=75
    c=12.5
    v=(g*m/c)*(1-np.exp(-t*c/m))
    return v
t = np.linspace(0,50,1000)
plt.plot(t, rate(v_o,t))

def rate_num(v_o, t):
    g=9.81
    m=75.0
    c=12.5
    v=np.zeros(len(t))
    v[0]=v_o
    for i in range(0, len(t)-1):
        v[i+1]=(t[i+1]-t[i]*(g-(c/m)*v[i])+v[i])
    return v

