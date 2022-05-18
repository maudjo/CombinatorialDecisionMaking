import pymzn;
import pathlib;

def readfile(filename):
    file = open(filename, 'r')
    f = file.readlines()
    
    rectangles={}
    i=0
    
    for line in f:
        if i==0:
           width_board = int(line)
           rectangles["w"] = int(line)
        elif i==1:
            num_fig = int(line)
            rectangles["n"] = int(line)
        else:
            line=line.strip()
            line=line.split(' ')
            rect=[ int(line[0]), int(line[-1])]
            rectangles["r"+str(i)] = rect
        i=i+1
        
    return rectangles

def ConvertToDzn(instance, data):
    file = open("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/"+ instance, "w+")
    pymzn.dict2dzn(data, fout='/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/newInstances/'+instance)
    file.close()

initial_count = 0
data=[]

for path in pathlib.Path("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances").iterdir():
    #if path.is_file():
     #   initial_count += 1
    data.append(path)



for i in range(len(data)):
   ConvertToDzn("ins"+str(i+1)+".dzn", readfile(data[i]))
   print(data[i])
