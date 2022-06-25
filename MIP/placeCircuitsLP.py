import gurobipy as gp 
import matplotlib.pyplot as plt

n = 12
w = 13
dx = [3,3,3,3,3,3,4,3,2,4,2,5]
dy = [3,4,5,6,7,8,4,3,4,2,3,2]



def placeRect(n,w,dx,dy):
    maxHeight = sum(dy);
    minHeight = max(dy);

    (Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

    model = gp.Model()

    startX = [ model.addVar(name = "x", vtype='I', lb=0, ub=w)for c in Circuits] 
    startY = [model.addVar( name = "y", vtype='I', lb=0, ub=maxHeight)for c in Circuits]
    h = model.addVar(name = "h", vtype='I', lb=minHeight, ub=maxHeight)


    b11 = [[[model.addVar( vtype='B') for i in range(4)] for j in X]for k in X]


    M1 = w
    M2 = h

    for c in Circuits:
        #all rectangles should be inside of plates length and final height h 
        model.addConstr(startX[c] + dx[c] <= w)
        model.addConstr(startY[c] + dy[c] <= h)
        #non overlapping constraint, using bigM and binary variables instead of the or condition 
        for j in Circuits:
            if c <j:
                model.addConstr(startX[c]+dx[c]<= startX[j] + M1*b11[c][j][0])
                model.addConstr(startX[j]+dx[j]<= startX[c] + M1*b11[c][j][1])
                model.addConstr(startY[c]+dy[c]<= startY[j] + M2*b11[c][j][2])
                model.addConstr(startY[j]+dy[j]<= startY[c] + M2*b11[c][j][3])
                


    for c in Circuits:
        for j in Circuits:
            sumb = 0; 
            for k in range(4):
                sumb +=  b11[c][j][k]
            model.addConstr(sumb <=3)
        if c<j and dx[c]*dy[c] < dx[j]*dy[j]:
            model.addConstr(startX[j] <= startX[c])
            model.addConstr(startY[j] <= startY[c])

    
    model.setObjective(h, gp.GRB.MINIMIZE)
    #model.tune()
    model.optimize()


    for j in Circuits:
        print("startX:" + str(startX[j].X) + "startY:" + str(startY[j].X))

    print(h)
    return h, startX,startY 

  

#sizes_circuits, n_circuits, width_plate = readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-1.txt")


print(placeRect(n,w,dx,dy))
h , startX, startY= placeRect(n,w,dx,dy)





