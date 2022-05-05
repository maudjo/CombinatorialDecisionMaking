
def readfile(filename):
    file = open(filename, 'r')
    f = file.readlines()
    
    rectangles=[]
    i=0
    
    for line in f:
        if i==0:
           width_board = int(line)
        elif i==1:
            num_fig = int(line)
        else:
            line=line.strip()
            line=line.split(' ')
            rect=[ int(line[0]), int(line[-1])]
            rectangles.append(rect) 
        i=i+1
        
    return rectangles, num_fig, width_board
