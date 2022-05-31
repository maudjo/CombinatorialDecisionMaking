include "globals.mzn";

int: k;
int: n;
int: nRectangles;
int: nShapes; 


set of int: DIMENSIONS = 1..k;
set of int: OBJECTS    = 1..n;
set of int: RECTANGLES = 1..nRectangles;
set of int: SHAPES     = 1..nShapes;

array[DIMENSIONS] of int:             l;
array[DIMENSIONS] of int:             u;
array[RECTANGLES,DIMENSIONS] of int:  rect_size;
array[RECTANGLES,DIMENSIONS] of int:  rect_offset;
array[SHAPES] of set of RECTANGLES:   shape;
array[OBJECTS,DIMENSIONS] of var int: x;
array[OBJECTS] of var SHAPES:         kind;

k = 2;                  % Number of dimensions for a 2D Plane
n = 4;           % Number of objects
nRectangles = 4;       % Number of rectangles
nShapes = 6;           % Number of shapes

l = [0, 0];
u = [8, 8];

constraint
    geost_bb(
        k,              % the number of dimensions
        rect_size,      % the size of each box in k dimensions
        rect_offset,    % the offset of each box from the base position in k dimensions
        shape,          % the set of rectangles defining the i-th shape
        x,              % the base position of each object.
                        % (var) x[i,j] is the position of object i in dimension j
        kind,           % (var) the shape used by each object
        l,              % array of lower bounds
        u               % array of upper bounds
    );

rect_size = [|
     5, 5|
     3, 3|
     3, 5|
     5, 3|];

rect_offset = [|
     0, 0|
     0, 0|
     0, 0|
     0, 0|];
     
     shape = [
    { 1 },
    
    { 2 },
    
    { 3 },
    { 4 },
    
    { 4 },
    { 3 } ];

array[OBJECTS] of set of SHAPES: valid_shapes;

valid_shapes = [{1}, {2}, {3,4},{5,6}];

constraint forall (obj in OBJECTS) (
    kind[obj] in valid_shapes[obj]
);

solve satisfy;