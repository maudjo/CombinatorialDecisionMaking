
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


print(readfile("/Users/maudjohansson/Combinatorial/Project/CombinatorialDecisionMaking/instances/ins-1.txt"))
