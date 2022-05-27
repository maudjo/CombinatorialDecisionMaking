include "globals.mzn";
include "diffn.mzn";
include "minisearch.mzn";
include "lns_min.mzn";

int: w; % width of the rectangle 
int: n; % number of rectangles

set of int: Circuits = 1..n; 

% width and length of 
array[Circuits] of int: dx; 
array[Circuits] of int: dy; 

% Upper bound for the height
int:maxHeight = sum(dy);
var 0..maxHeight:endY; 

%variables for x and y positions 
array[Circuits] of var 0..w: startX;
array[Circuits] of var 0..maxHeight: startY;


% the height of the rectangle cant be bigger than the height of all the circuits combined 
constraint forall(c in Circuits)(startY[c] +dy[c] <= maxHeight);

% circuits must be inside of rectangle 
constraint forall(c in Circuits)(startX[c] +dx[c] <= w);


% no overlapping rectangles 
constraint diffn(startX, startY, dx,dy);

%makespan (returns the maximum height given the circuits positions)
var int: makespan = max(cir in Circuits)(startY[cir] + dy[cir]);
%var int: h = max(startY)

int: iterations = 100;
float: destructionRate = 0.3;
solve search minimize_bab(makespan); 
%solve lns_min(makespan, startY, iterations, destructionRate);

%solve minimize makespan; 
output [ "x-koordinates = \(startX)\nwidth = \(w)\ny-koordinates = \(startY)\nheight = \(makespan)\n" ];











