include "globals.mzn";
include "geost.mzn";

int: w; % width of the rectangle 
int: n; % number of circuits
int: o; %number of different offsets (2*n)

set of int: Circuits = 1..n; 
set of int: Offsets = 1..o;  

%array for the rectangle offsets, 1..4 indicates xoffset,yoffset,width,height
array[Offsets, 1..4] of int: rectOffsets; 

%different shapes for the rectangles, each rectangle can take two different shapes
array[int] of set of Offsets: shape; 

% width and length of the different circuits
array[Circuits] of int: dx; 
array[Circuits] of int: dy; 


% Upper and lower bound for the height
int:maxHeight =max(sum(dx), sum(dy));
int:minHeight = min(max(dx), max(dy));
var minHeight..maxHeight:endY; 

%variables for x and y positions 
array[Circuits] of var 0..w: startX;
array[Circuits] of var 0..maxHeight: startY;
 
%get the offset of each circuit      
array[Offsets,1..2] of int: off =array2d(Offsets, 1..2,
      [rectOffsets[i,j] | i in Offsets, j in 1..2]);

% get the size of each circuit
array[Offsets,1..2] of int: size =array2d(Offsets, 1..2,
      [rectOffsets[i,j] | i in Offsets, j in 3..4]);

%adding the coordinates for each circuit in x direction=1 and y direction=2   
array[Circuits,1..2] of var int: coordinate;
constraint forall(i in Circuits)
   (coordinate[i,1] = startX[i] /\ coordinate[i,2] = startY[i]);

%array consisting of the valid shape for each circuit 
array[Circuits] of set of int: validshapes;
% get the final shape for each circuit 
array[Circuits] of var int: kind;
constraint forall(i in Circuits)(kind[i] in validshapes[i]);

%global non-overlapping constraint that also enforces all objects to fit inside a box of given bounds [0,0] and [w,endY]
constraint geost_bb(2,size,off,shape,coordinate,kind,[ 0,0 ],[ w, endY ]);

%symmetry breaking, add lexicographical ordering on circuits of same size
array[int] of int: EqualCircuits = [
  c | c in Circuits, d in Circuits where c != d /\ dx[c] = dx[d] /\ dy[c] = dy[d]]; 

constraint forall(c in Circuits)(
  if length(EqualCircuits) > 1 /\ c in EqualCircuits then 
    forall(j in EqualCircuits where j>c)(
      if dx[c] = dx[j] then 
        lex_greater([startX[j], startY[j]],[startX[c], startY[c]])
      else true endif 
    )else true endif
);


%order the circuits from biggest to smallest
constraint forall(c,j in Circuits where c< j /\ dx[c]*dy[c] < dx[j]*dy[j])
  (lex_greater([startX[j], startY[j]], [startX[c], startY[c]])
  ); 

solve minimize endY;

output ["h = \(endY);\nx = \(startX);\ny = \(startY);\nkind = \(kind);\n"];