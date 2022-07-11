import pymzn;
import pathlib;

def readfile(filename):
    file = open(filename, 'r')
    f = file.readlines()
    rectangles={"dx":[], "dy":[]}
    geost ={"rectOffsets": "|", "shape": [], "validshapes": [],"dx":[], "dy":[]}
    i=0
    
    for line in f:
        if i==0:
           rectangles["w"] = int(line)
           geost["w"] = int(line)
        elif i==1:
            rectangles["n"] = int(line)
            geost["n"] = int(line)
            geost["o"]=2*int(line)
            k = 0
            for j in range(int(line)):
                geost["shape"].append({j+1 + k})
                geost["shape"].append({j+2+k})
                geost["validshapes"].append("{" + str(j+1 + k) +"," + str(j+2 + k) +"}")
                k +=1
        else:
            line=line.strip()
            line=line.split(' ')
            rectx=int(line[0])
            recty= int(line[-1])
            rectangles["dx"].append(rectx)
            rectangles["dy"].append(recty)
            geost["dx"].append(rectx)
            geost["dy"].append(recty)
            geost["rectOffsets"]+= "0,0," + str(rectx) + "," + str(recty) + "|" 
            geost["rectOffsets"]+= "0,0," + str(recty) + "," + str(rectx) + "|"        
        i=i+1
    
    geost["rectOffsets"] = [geost["rectOffsets"]]
        
    return rectangles, geost


def ConvertToDzn(instance, data, type = None):
    if(type=="noRot"):
        file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/"+ instance, "w+")
        pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/'+instance)
        file.close()
    else:
        file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstancesRotation/"+ instance, "w+")
        pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstancesRotation/'+instance)
        file.close()

data=[]

for path in pathlib.Path("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances").iterdir():
    data.append(path)

for i in range(len(data)):
    noRot, geost = readfile(data[i])
    #ConvertToDzn("ins"+str(i+1)+".dzn", noRot, "noRot")
    #ConvertToDzn("insRot"+str(i+1)+".dzn", geost)
