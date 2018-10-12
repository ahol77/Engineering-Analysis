import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**5 - 6*x**3 + np.pi*x - 1
    #return np.exp(-x/3) + x**4 - 7*x**2*np.log(x)
    #return x**12 + 2**x - 2.5

def ROOT_FALSEPOSITION(b,a,f,err):
    c = b - ((f(b))*(a-b))/((f(a))-(f(b)))
    z = 0
    clist = []
    while np.abs(f(c)) > err:
        if f(a)*f(b) < 0:
            b=c
        else:
            a=c
        clist = np.append(clist,c)
        c = b - ((f(b))*(a-b))/((f(a))-(f(b)))
        z += 1
    iterations = np.arange(1,z+1,1)
    est_root = f(clist)
    rel_err = np.abs(est_root/f(c) - 1)*100
    plt.close('all')
    plt.figure(1)
    plt.subplot(211)
    plt.plot(iterations, clist, 'bo--')
    plt.xlabel("Number of Iterations", fontsize=10, fontstyle='italic')
    plt.ylabel("Estimate of Root", fontsize=10, fontstyle='italic')
    plt.title("How False Position Method Approaches Actual Root",fontsize=14)
    plt.subplots_adjust(hspace = .7)

    plt.subplot(212)
    plt.plot(iterations, rel_err, 'ro--')
    plt.xlabel("Number of Iterations", fontsize=10, fontstyle='italic')
    plt.ylabel("Relative Error", fontsize=10, fontstyle='italic')
    plt.title("Relative Error Progression",fontsize=14)
    plt.show()
    return c, z

print(ROOT_FALSEPOSITION(1.5,2.5,f,0.0001))
