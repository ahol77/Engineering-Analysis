import numpy as np
from matplotlib import pyplot as plt

def f(z):
    f[0] = pow(x-4,2) + pow(y-4,2) - 5
    f[1] = pow(x,2) + pow(y,2) - 

def bisect(f,a,b,tol):
    rootlist=[]
    infblock=0
    while infblock==0:
        c=(a+b)/2
        if f(c)==0:
            rootlist=np.append(rootlist,[c])
            infblock=1
        elif (b-a)< tol:
            infblock=1
            if f(a)*f(b)<0:
                rootlist=np.append(rootlist,[c])
            else:
                print("root not found")
        else:
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
    return rootlist

def manyintervals(f,a,b,tol,inte,derivf):
    rootlist=[]
    intsize=(b-a)/inte
    minimum=a
    maximum=a+intsize
    loopend=0
    while loopend<inte:
        if f(minimum)*f(maximum)<0:
            r1 = bisect(f,minimum,maximum,tol)
            rootlist = np.append(rootlist, r1)
        minimum=minimum+intsize
        maximum=maximum+intsize
        loopend=loopend+1
    print(rootlist)

manyintervals()