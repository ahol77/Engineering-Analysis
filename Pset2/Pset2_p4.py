import numpy as np
from matplotlib import pyplot as plt
import math as m
#Number you will iterate up to in the summation
n = 100
#Factorial Function
def fact(x):
    p = 1
    #Check if variable is integer
    if type(x) is int:
        while x >=1:
            p *= x
            x -= 1
        return p
    #Check if variable is 0
    elif x == 0:
        return 1
    #Stop program if not an integer
    else:
        print("Need an Integer for Factorial")
        quit()

#Odd Factorial Function, same flow as normal factorial but with -2 to only get odd numbers
def odd_fact(x):
    p = 1
    if type(x) is int:
        while x >=1:
            p *= x
            x -= 2
        return p
    elif x == 0:
        return 1
    else:
        print("Need an Integer for Factorial")
        quit()

#Sum function
def mysum(n):
    summ = 0
    #Iterate over the the range of 0 to n which is previously defined
    for i in range(n):
        numerator = fact(i)
        denominator = odd_fact(2*i+1)
        total = 2* numerator / denominator
        summ += total
    return summ

#Generate x array of integers
x = np.arange(0,n+1,1)
#Generate y array dependent on each individual n value in the x array
y = [mysum(i) for i in x]

#PART (II)
plt.close('all')

plt.plot(x, y,'b')
plt.xlabel('n', fontsize=14, fontstyle='italic')
plt.ylabel('alpha', fontsize=14, fontstyle='italic')
plt.title("alpha vs n",fontsize=18)

plt.show()

#PART (III)
z = mysum(1000)
print(z) # which is 3.1415926535... aka pi

#PART (IV)
def new_fact(x):
    if x % 2 == 1:
        n = (x+1)/2
        return m.factorial(2*n) / (2**n * m.factorial(n))
    else:
        return 2**x * m.factorial(x)

z = new_fact(4)
print(z)

