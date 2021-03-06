
import gurobipy as gp 
import matplotlib.pyplot as plt
import numpy as np

def readfile(filename):
    file = open(filename, 'r')
    f = file.readlines()
    rectangles={"dx":[], "dy":[]}
    i=0

    for line in f:
        if i==0:
           rectangles["w"] = int(line)
        elif i==1:
            rectangles["n"] = int(line)
        else:
            line=line.strip()
            line=line.split(' ')
            rectx=int(line[0])
            recty= int(line[-1])
            rectangles["dx"].append(rectx)
            rectangles["dy"].append(recty)
        i=i+1
    return rectangles


# Changing boundary conditions as rotation is possible
def placeRectWithRot(n,w,dx,dy):
    maxHeight = sum(dy);
    minHeight = min(min(dy),min(dx))

    (Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

    model = gp.Model()

    startX = [ model.addVar(name = "x", vtype='I', lb=0, ub=w)for c in Circuits] 
    startY = [model.addVar( name = "y", vtype='I', lb=0, ub=maxHeight)for c in Circuits]
    endY= model.addVar(name = "endY", vtype='I', lb=minHeight, ub=maxHeight)

# b11 represents two circuits relative positions for all circuits.
    bin = [[[model.addVar( vtype='B') for i in range(4)] for j in X]for k in X]
# Rotated represents for each circuit whether it is rotated(1) or not(0)
    rotated =[model.addVar(vtype='B') for c in Circuits]

    M1 = w
    M2 = endY

    for c in Circuits:
        # Possible change of dimentions because of rotation
        dxRot = dx[c]*(1-rotated[c]) + dy[c]*rotated[c]
        dyRot = dy[c]*(1-rotated[c]) + dx[c]*rotated[c]
        
        #all rectangles should be inside of plates length and final height h 
        model.addConstr(startX[c]+dxRot  <= w)
        model.addConstr(startY[c]+dyRot <= endY)
        
        #non overlapping constraint, using bigM and binary variables instead of the or condition 
        for j in Circuits:
            # Possible change of dimentions because of rotation
            dxRot_j = dx[j]*(1-rotated[j]) + dy[j]*rotated[j]
            dyRot_j = dy[j]*(1-rotated[j]) + dx[j]*rotated[j]
            if c <j:
                model.addConstr(startX[c]+ dxRot   <= startX[j]  + M1*bin[c][j][0])
                model.addConstr(startX[j]+ dxRot_j <= startX[c]  + M1*bin[c][j][1])
                model.addConstr(startY[c]+ dyRot   <= startY[j]  + M2*bin[c][j][2])
                model.addConstr(startY[j]+ dyRot_j <= startY[c]  + M2*bin[c][j][3])


    for c in Circuits:
        for j in Circuits:
            sumb = 0; 
            for k in range(4):
                sumb +=  bin[c][j][k]
            model.addConstr(sumb <=3)
        if c<j and dx[c]*dy[c] < dx[j]*dy[j]:
            model.addConstr(startX[j] <= startX[c])
            model.addConstr(startY[j] <= startY[c])

    model.setObjective(endY, gp.GRB.MINIMIZE)
    model.optimize()
    
    startxVal=[]
    startyVal = []
    rotated = []
    
    for j in Circuits:
        print("startX:" + str(startX[j].X) + "  startY:" + str(startY[j].X))
        #print("rotated: " + str(rotated[j])+ "\n")
        startxVal.append(str(abs(startX[j].X)))
        startyVal.append(str(abs(startY[j].X)))
        #rotated.append(str(rotated[j].X))
    print(rotated)
    print(endY)
    return endY.X, startxVal,startyVal



rect = readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-12.txt")


endY, startX, startY= placeRectWithRot(rect["n"],rect["w"],rect["dx"],rect["dy"])


def writeToFile(instance):
    file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/resultsLP/rotation/"+ instance, "w+")
    file.write(str(rect["w"]) + " " + str(endY) + "\n")
    file.write(str(rect["n"])+ "\n")
    for i in range (rect["n"]):
        file.write(str(rect["dx"][i]) +" " + str(rect["dy"][i])+" "+str(startX[i])+" "+str(startY[i]) + "\n")
    file.close()

writeToFile("out-12.txt")