import random
from random import randrange

from math import dist
from math import comb

import numpy
import numpy as np
#from numpy import random, unique, square, power, linalg, argmax, array, mean, arange

from matplotlib.pyplot import axis, plot, figure, show, legend, scatter, xlabel, ylabel, title, colorbar
from matplotlib.pyplot import bar, grid, xticks, hist
import matplotlib.pyplot as plt


vektor=[0,0,1,1,2,2,3,3,3,4]
num_simulations=20000
countA=0
countP=0
countZ=0
Z=[]

for _ in range(num_simulations):
    urn = np.array([0] * 2 + [1] * 2 + [2] * 2 + [3] * 3 + [4] * 1)
    #print(urn)
    numbers = np.random.choice(urn, size=3, replace=True)
    #numbers=random.sample([0,1,2,3,4], counts=[2,2,2,3,1], k=3)
    cnt=0
    if numbers[0]==0 and numbers[2]==3:
        countA+=1

    if numbers[0]*numbers[1]*numbers[2]==1:
        countP+=1

    if numbers[0]==numbers[1] and numbers[2]!=3:
        if numbers[0]==3:
            countZ+=1

    if numbers[1]==numbers[2] and numbers[0]!=3:
        if numbers[1]==3:
            countZ+=1

    if numbers[0]==numbers[2] and numbers[1]!=3:
        if numbers[0]==3:
            countZ+=1

    for number in numbers:
        if number==3:
            cnt+=1
    Z.append(cnt)

#a
print("P(W1=0)mit(W3=3) = ",countA/num_simulations)
print("P(W1*W2*W3=1) = ",countP/num_simulations)
print("P(Z=2) = ",countZ/num_simulations)
print("\n")


z, count = numpy.unique(Z, return_counts=True)
bar(z, count / num_simulations, width=0.9, color="red", edgecolor="black", label="relative Haufigkeiten")
xticks(range(0, 5))
grid()
show()

#b
#w1*w2*w3=2 ---> 1 1 2   1 2 1  2 1 1
p1=2/10*2/10*2/10 + 2/10*2/10*2/10 + 2/10*2/10*2/10
print("P(W1*W2*W3=2) = ",p1)

#P(Z=2)
p2=3/10*3/10*7/10 + 3/10*7/10*3/10 + 7/10*3/10*3/10
print("P(Z=2) = ",p2)



