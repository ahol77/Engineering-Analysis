import numpy as np

def gauss_elim(mat, b):
    dims=mat.shape
    if len(dims)!=2:
        print('ERROR')
        return
    elif dims[0]!=dims[1]:
        print('ERROR')
        return
    n=dims[0]
    for i in range(0,n):
        for j in range(i+1,n):
            fac=float(mat[j,i])/mat[i,i]
            for k in range(i,n):
                mat[j,k]-=fac[i,k]
            b[j]-=fac*b[i]
    x=np.zeros(n)
    x[n-1]=b[n-1]/mat[n-1,n-1]
    for i in range(n-1,-1,-1):
        su=b[i]
        for j in range(i+1,n):
            su-=mat[i,j]*x[j]
        x[i]=su/mat[i,i]
    return x
    

    