import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
cmap = colors.ListedColormap(['peachpuff','pink','lightblue','thistle','lemonchiffon'])


w=8
l=8
n=4
c1=[3,3,0,0]
c2=[3,5,0,3]
c3=[5,3,3,0]
c4=[5,5,3,3]


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
