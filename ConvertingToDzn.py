import pymzn;
import pathlib;

def readfile(filename):
    file = open(filename, 'r')
    f = file.readlines()
    rectangles={"dx":[], "dy":[]}
    geost ={"rect_size":"|", "rect_offset": "|", "shape": [], "valid_shapes": []}
    i=0
    
    for line in f:
        if i==0:
           rectangles["w"] = int(line)
        elif i==1:
            rectangles["n"] = int(line)
            k = 0
            for j in range(int(line)):
                geost["rect_offset"]+= "0,0 |"
                geost["shape"].append({j+1})
                geost["valid_shapes"].append("{" + str(j+1 + k) +"," + str(j+2 + k) +"}")
                k +=1
        else:
            line=line.strip()
            line=line.split(' ')
            rectx=int(line[0])
            recty= int(line[-1])
            rectangles["dx"].append(rectx)
            rectangles["dy"].append(recty)
            geost["rect_size"] += str(rectx) + "," + str(recty) + "|"
        i=i+1
    geost["rect_offset"] = [geost["rect_offset"]]
    geost["rect_size"] = [geost["rect_size"]]
        
    return rectangles, geost

rectangles, geost = readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-2.txt")
print(readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-2.txt"))

def ConvertToDzn(instance, data, type = None):
    if(type=="rectangles"):
        file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/"+ instance, "w+")
        pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/'+instance)
        file.close()
    else:
        file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances2/"+ instance, "w+")
        pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances2/'+instance)
        file.close()

data=[]

for path in pathlib.Path("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances").iterdir():
    data.append(path)

for i in range(len(data)):
    rectangles, geost = readfile(data[i])
    #ConvertToDzn("ins"+str(i+1)+".dzn", rectangles, "rectangles")
    ConvertToDzn("ins"+str(i+1)+".dzn", geost)
    print(data[i])
