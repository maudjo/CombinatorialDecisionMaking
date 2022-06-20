from mip import Model, xsum, BINARY, INTEGER, minimize 

n = 3
w = 10
dx = [2,3,3]
dy = [4,3,3]
maxHeight = sum(dy);
minHeight = max(dy);

(Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

model = Model()

startX = [{c: model.add_var(var_type=INTEGER, lb=0, ub=w)} for c in Circuits]
startY = [{c: model.add_var( var_type=INTEGER, lb=minHeight, ub=maxHeight)} for c in Circuits]
endY = {max(startY[c] +dy[c]):  model.add_var(var_type = INTEGER)for c in Circuits}
b1 = [[model.add_var(name="b({},{})".format(i, j), var_type=BINARY) for i in X] for j in X]
b2 = [[model.add_var(name="b({},{})".format(i, j), var_type=BINARY) for i in Y] for j in Y]

M1 = w
M2 = endY
#circuits must be inside of rectangle 
for c in Circuits:
    model.add_constr(startX[c] + dx[c] <= w)
    model.add_constr(startY[c] + dy[c] <= endY)
    model.add_constr(startX[c]+dx[c]<= startX[j] + M1*b1[c,j] for j in X)
    model.add_constr(startX[j]+dx[j]<= startX[c] + M1*b1[c,j] for j in X)
    model.add_constr(startY[c]+dy[c]<= startY[j] + M2*b2[c,j] for j in X)
    model.add_constr(startY[j]+dy[j]<= startY[c] + M2*b2[c,j] for j in X)

for x in X:
    model.add_constr(xsum(b1[x][j] for j in Circuits ) == 1 )

for y in Y:
    model.add_constr(xsum(b2[y][j] for j in Circuits ) == 1 )


#model.objective = minimize(max(startY[c] +dy[c] for c in Circuits))
model.objective = minimize(endY)
model.optimize()




