'''
Pseduocode:

a = some positive number 
IF a > 0 THEN
    tol = 10**-5
    x = a/2
    DO
        y = (x+a/x)/2
        e = ABSOLUTE_VALUE((y-x)/y)
        x = y
        IF e < tol EXIT
    ENDDO
ELSE
    x = 0
ENDIF

PRINT x
'''
import numpy as np

def sqr_root(a,t):
    #Check if a is a positive number to initate sqr root process
    if a > 0:
        #Take half of initial input
        x = a/2
        iteration = 0
        while True:
            #Sqr root approximation
            y = (x+a/x)/2
            #Error
            e = np.abs((y-x)/y)
            x = y
            iteration += 1
            #Check if error is less than tolerance
            if e < t:
                break
    #If not a positive number, than simply return 0 as the sqr root
    else:
        x = 0
        iteration = 1
    print(x, iteration)
        
sqr_root(-9, 0.001) # Root = 0, Iterations = 1
sqr_root(0, 0.001) # Root = 0, Iterations = 1
sqr_root(9, 0.001) # Root = 3.0000000000393214, Iterations = 4
sqr_root(99, 0.001) # Root = 9.949874371159666, Iterations = 6
sqr_root(9999, 0.001) # Root = 99.99500012910633, Iterations = 9
sqr_root(999999, 0.001) # Root = 999.9996532976936, Iterations = 12




