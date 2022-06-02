from stringprep import c8_set
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
cmap = colors.ListedColormap(['peachpuff','pink','lightblue','thistle','lemonchiffon', 'peachpuff','pink','lightblue','thistle','lemonchiffon', 'peachpuff','pink','lightblue','thistle','lemonchiffon','peachpuff','pink','lightblue','thistle','lemonchiffon'])


w=30
l=30
n=20
c1=[3,3,27,0]
c2=[3,4,21,7]
c3=[3,5,0,25]
c4=[3,6,24,24]
c5=[3,7,17,0]
c6=[3,8,27,13]
c7=[3,9,27,21]
c8=[3,10,27,3]
c9=[3,11,24,0]
c10=[3,13,24,11]
c11=[3,14,18,16]
c12=[3,16,14,0]
c13=[3,19,21,11]
c14=[3,25,0,0]
c15=[4,3,20,0]
c16=[4,4,20,3]
c17=[4,6,14,24]
c18=[4,8,14,16]
c19=[4,9,17,7]
c20=[11,30,3,0]



solution=[w,l,n,c1,c2,c3,c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]


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
