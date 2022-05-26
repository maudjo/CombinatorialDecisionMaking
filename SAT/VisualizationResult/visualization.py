import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
cmap = colors.ListedColormap(['peachpuff','pink','lightblue','thistle','lemonchiffon', 'peachpuff','pink','lightblue','thistle','lemonchiffon', 'peachpuff','pink','lightblue','thistle','lemonchiffon','peachpuff','pink','lightblue','thistle','lemonchiffon','peachpuff','pink','lightblue','thistle','lemonchiffon'])


w=10
l=11
n=6
c1=[3,7,3,3]
c2=[0,7,3,4]
c3=[6,6,3,5]
c4=[6,0,3,6]
c5=[3,0,3,7]
c6=[0,0,3,7]


solution=[w,l,n,c1,c2,c3,c4]


def makeSolutionCoordinates(solution):
    solutionCoordinates = [[0 for x in range(solution[0])] for y in range(solution[1])] 
    circuits=solution[3:]
    color =1
    for c in circuits:
        x=c[2]
        y=c[3]
        w=c[0]
        h=c[1]
        for i in range(w):
            for j in range(h):
                solutionCoordinates[x+i][y+j]=color
        color +=1
    return solutionCoordinates


solutionCoordinates=makeSolutionCoordinates(solution)

plt.figure(figsize=(w,l))
plt.pcolor(solutionCoordinates[::-1],cmap=cmap,edgecolors='k', linewidths=3)
plt.show()
