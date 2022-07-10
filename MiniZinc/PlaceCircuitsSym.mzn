include "globals.mzn";
include "diffn.mzn";
include "cumulative.mzn";
include "lex_greater.mzn"; 
include "lex_less.mzn";

int: w; % width of the rectangle 
int: n; % number of rectangles

set of int: Circuits = 1..n; 

% width and length of 
array[Circuits] of int: dx; 
array[Circuits] of int: dy; 

% Upper and lower bound for the height
int:maxHeight = sum(dy);
int:minHeight = max(dy);
var minHeight..maxHeight:endY; 

%variables for x and y positions 
array[Circuits] of var 0..w: startX;
array[Circuits] of var 0..maxHeight: startY;

% RAGNA: jeg skjønner ikke helt denne kodelinjen lenger... Jeg synes det ser ut som at det ikke er en summering her?
% the height of the rectangle cant be bigger than the height of all the circuits combined 
constraint forall(c in Circuits)(startY[c] +dy[c] <= endY);

% circuits must be inside of rectangle 
constraint forall(c in Circuits)(startX[c] +dx[c] <= w );

%add redundant cumulativ constraints to improve propagation
%may be able to do things before diffn kick in 
constraint cumulative(startX, dx, dy, endY);
constraint cumulative(startY, dy, dx, w);


% global constraint for no overlapping rectangles
constraint diffn(startX, startY, dx,dy);

%local constraint for overlapping 
%constrain forall(c1,c2 in Circuits where c1 < c2)
%(
%        startX[c1] + dx[c1] <= startX[c2]  \/
%        startX[c2] + dx[c2] <= startX[c1]  \/
%        startY[c1] + dy[c1] <= startY[c2] \/
%        startY[c2] + dy[c2] <= startY[c1]
%)

% Symmetry breaking rules
constraint startX[1] <= 1/2*(w-dx[1]);
%constraint startY[1] <= 1/2*(makespan-dy[1]); Får ikke denne til å funke


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

%symmetry breaking constraint 
%constraint symmetry_breaking_constraint(forall(c in Circuits)(startX[c] <= 1/2*(w-startX[c]))); 


solve minimize endY; 

%result
output [ "x-koordinates = \(startX)\nwidth = \(w)\ny-koordinates = \(startY)\nheight = \(endY)\n" ];











