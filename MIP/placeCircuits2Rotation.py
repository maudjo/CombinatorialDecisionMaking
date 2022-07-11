
import gurobipy as gp 
import matplotlib.pyplot as plt
import numpy as np

n = 8
w = 12
dx = [3, 3, 3, 3, 3, 3, 3, 6]
dy = [3, 4, 5, 6, 7, 8, 9, 3]


# Changing boundary conditions as rotation is possible
def placeRectWithRot(n,w,dx,dy):
    maxHeight = sum(dy);
    #minHeight = max(dy);  
    minHeight = min(min(dy),min(dx))

    (Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

    model = gp.Model()

    startX = [ model.addVar(name = "x", vtype='I', lb=0, ub=w)for c in Circuits] 
    startY = [model.addVar( name = "y", vtype='I', lb=0, ub=maxHeight)for c in Circuits]
    h = model.addVar(name = "h", vtype='I', lb=minHeight, ub=maxHeight)

# b11 represents two circuits relative positions for all circuits.
    b11 = [[[model.addVar( vtype='B') for i in range(4)] for j in X]for k in X]
# Rotated represents for each circuit whether it is rotated(1) or not(0)
    rotated =[model.addVar(vtype='B') for c in Circuits]

    M1 = w
    M2 = h

    for c in Circuits:
        # Possible change of dimentions because of rotation
        dxRot = dx[c]*(1-rotated[c]) + dy[c]*rotated[c]
        dyRot = dy[c]*(1-rotated[c]) + dx[c]*rotated[c]
        
        #all rectangles should be inside of plates length and final height h 
        model.addConstr(startX[c]+dxRot  <= w)
        model.addConstr(startY[c]+dyRot <= h)
        
        #non overlapping constraint, using bigM and binary variables instead of the or condition 
        for j in Circuits:
            # Possible change of dimentions because of rotation
            dxRot_j = dx[j]*(1-rotated[j]) + dy[j]*rotated[j]
            dyRot_j = dy[j]*(1-rotated[j]) + dx[j]*rotated[j]
            if c <j:
                model.addConstr(startX[c]+ dxRot   <= startX[j]  + M1*b11[c][j][0])
                model.addConstr(startX[j]+ dxRot_j <= startX[c]  + M1*b11[c][j][1])
                model.addConstr(startY[c]+ dyRot   <= startY[j]  + M2*b11[c][j][2])
                model.addConstr(startY[j]+ dyRot_j <= startY[c]  + M2*b11[c][j][3])
           

    for c in Circuits:
        for j in Circuits:
            sumb = 0; 
            sumb2 = 0; 
            for k in range(4):
                sumb +=  b11[c][j][k]
            model.addConstr(sumb <=3)
        #if c<j and dx[c]*dy[c] < dx[j]*dy[j]:
         #   model.addConstr(startX[j] <= startX[c])
          #  model.addConstr(startY[j] <= startY[c])

    model.setObjective(h, gp.GRB.MINIMIZE)
    model.optimize()
    
    for j in Circuits:
        print("startX:" + str(startX[j].X) + "  startY:" + str(startY[j].X))
        print("rotated: " + str(rotated[j])+"\n")

    print(h)
    return h, startX,startY 

#sizes_circuits, n_circuits, width_plate = readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-1.txt")


print(placeRectWithRot(n,w,dx,dy))
h , startX, startY= placeRectWithRot(n,w,dx,dy)
