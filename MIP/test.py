
from mip import Model, xsum, BINARY, INTEGER, minimize 
import gurobipy as gp 

n = 3
w = 10
dx = [2,3,3]
dy = [4,3,3]
maxHeight = sum(dy);
minHeight = max(dy);

(Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

model = gp.Model()

startX = [ model.addVar(vtype=INTEGER, lb=0, ub=w)for c in Circuits] 
startY = [model.addVar( vtype=INTEGER, lb=minHeight, ub=maxHeight)for c in Circuits]
#endY =  model.add_var(for c in Circuits max(startY[c] +dy[c]),  var_type = INTEGER)
b1 = [[model.addVar(name="b({},{})".format(i, j), vtype=BINARY) for i in X] for j in X]
b2 = [[model.addVar(name="b({},{})".format(i, j), vtype=BINARY) for i in Y] for j in Y]

mi = w
M2 = w*2
#circuits must be inside of rectangle 
for c in Circuits:
    model.addConstr(startX[c] + dx[c] <= w)
   #model.addConstr(startY[c] + dy[c] <= max(startY[c] +dy[c]) for c in Circuits)
    model.addConstr(startX[c]+dx[c]<= startX[j] + mi*b1[c,j] for j in X)
    model.addConstr(startX[j]+dx[j]<= startX[c] + mi*b1[c,j] for j in X)
    model.addConstr(startY[c]+dy[c]<= startY[j] + M2*b2[c,j] for j in X)
    model.addConstr(startY[j]+dy[j]<= startY[c] + M2*b2[c,j] for j in X)

for x in X:
    model.addConstr(xsum(b1[x][j] for j in Circuits ) == 1 )

for y in Y:
    model.addConstr(xsum(b2[y][j] for j in Circuits ) == 1 )


#model.objective = minimize(max(startY[c] +dy[c] for c in Circuits))
model.objective = minimize(max(startY[c] +dy[c]) for c in Circuits)
model.optimize()
