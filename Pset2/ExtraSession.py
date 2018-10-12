import numpy as np

def f(x):
    return x**4-6*x**3+12*x**2-10*x+3

def derivf(x):
    return 4*x**3-18*x**2+24*x-10

def bisect(f,a,b,tol,derivf):
    rootlist=[]
    multiroot=[]
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
                if np.abs(derivf(c))<tol:
                    multiroot=np.append(multiroot,[c])
            else:
                print("root not found")
        else:
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
    return rootlist, multiroot

def manyintervals(f,a,b,tol,inte,derivf):
    rootlist=[]
    multiroot=[]
    intsize=(b-a)/inte
    minimum=a
    maximum=a+intsize
    loopend=0
    while loopend<inte:
        if f(minimum)*f(maximum)<0:
            r1, r2 = bisect(f,minimum,maximum,tol)
            rootlist = np.append(rootlist, r1)
            isitmulti=np.size()
            if isitmulti>0:
                multiroot=np.append(r2)
        minimum=minimum+intsize
        maximum=maximum+intsize
        loopend=loopend+1
    print(rootlist, multiroot)

manyintervals(f,-2,10,0.001,1000, derivf)
        