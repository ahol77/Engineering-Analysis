import numpy as np
from matplotlib import pyplot as plt
import FalsePosition as f
from scipy import optimize as o
import timeit as t

def manytests(tests,method,a,b,f,err,derivf,inte):
    if method == fp:
        for i in range(0,tests):
            f.manyintervals(a,b,f,derivf,err,inte)
    elif method == brentq:
        
    else:
        print('Please enter "brentq" or "fp" for the method variable.')
    
t.timeit(f.manyintervals(1.5,2.5,f.f1,derivf1,0.0001,10))
print(o.brentq(f.f1,1.5,2.5,xtol = 0.0001))

