import pathlib
import gurobipy as gp 
import matplotlib.pyplot as plt


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

def placeRect(n,w,dx,dy):
    maxHeight = sum(dy);
    minHeight = max(dy);

    (Circuits, X, Y) = (range(n), range(len(dx)), range(len(dy)))

    #defining the gurobi model 
    model = gp.Model()

    #setting the variables for position and the end height 
    startX = [ model.addVar(name = "x", vtype='I', lb=0, ub=w)for c in Circuits] 
    startY = [model.addVar( name = "y", vtype='I', lb=0, ub=maxHeight)for c in Circuits]
    endY = model.addVar(name = "endY", vtype='I', lb=minHeight, ub=maxHeight)

    #binary constraint used for non-overlapping rectangles constraint
    bin = [[[model.addVar( vtype='B') for i in range(4)] for j in X]for k in X]

    #setting as small M as possible 
    M1 = w
    M2 = endY

    for c in Circuits:
        #all rectangles should be inside of plates width and final height endY
        model.addConstr(startX[c] + dx[c] <= w)
        model.addConstr(startY[c] + dy[c] <= endY)

        #non overlapping constraint, using bigM and binary variables instead of the or condition 
        for j in Circuits:
            if c <j:
                model.addConstr(startX[c]+dx[c]<= startX[j] + M1*bin[c][j][0])
                model.addConstr(startX[j]+dx[j]<= startX[c] + M1*bin[c][j][1])
                model.addConstr(startY[c]+dy[c]<= startY[j] + M2*bin[c][j][2])
                model.addConstr(startY[j]+dy[j]<= startY[c] + M2*bin[c][j][3])
                


    for c in Circuits:
        for j in Circuits:
            sumb = 0; 
            for k in range(4):
                sumb +=  bin[c][j][k]
            model.addConstr(sumb <=3)
        #sorting the rectangles so that the biggest rectangles are placed first 
            if c<j and dx[c]*dy[c] < dx[j]*dy[j]:
                model.addConstr(startX[j] <= startX[c])
                model.addConstr(startY[j] <= startY[c])
    
    #symmetry breaking constraint
    model.addConstr(max(startX) <= (1/2)*(w-dx[0]))

    
    model.setObjective(endY, gp.GRB.MINIMIZE)
    model.optimize()
    
    startxVal=[]
    startyVal = []


    for j in Circuits:
        print("startX:" + str(startX[j].X) + "startY:" + str(startY[j].X))
        startxVal.append(str(abs(startX[j].X)))
        startyVal.append(str(abs(startY[j].X)))
    print(endY)
    return endY.X, startxVal,startyVal

  

rect = readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-1.txt")

endY, startX, startY= placeRect(rect["n"],rect["w"],rect["dx"],rect["dy"])


def writeToFile(instance):
    file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/resultsLP/noRot/"+ instance, "w+")
    file.write(str(rect["w"]) + " " + str(endY) + "\n")
    file.write(str(rect["n"])+ "\n")
    for i in range (rect["n"]):
        file.write(str(rect["dx"][i]) +" " + str(rect["dy"][i])+" "+str(startX[i])+" "+str(startY[i]) + "\n")
    file.close()

#writeToFile("out-1.txt")









