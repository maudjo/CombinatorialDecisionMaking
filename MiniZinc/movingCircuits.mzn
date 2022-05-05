include "cumulative.mzn";

enum OBJECTS;
array[OBJECTS] of int: dx; 
array[OBJECTS] of int: dy; 



int: width;

array[OBJECTS] of var 0..width: startX;
array[OBJECTS] of var 0..width: startY;


int: length = sum (dy);
var 0..length: endY;

constraint cumulative(startX, dx, dy, width);
constraint cumulative(startY, dx, dy, endY);
 
constraint forall(o in OBJECTS)(startX[o] +dx[o] <= width);
constraint forall(o in OBJECTS)(startY[o] +dy[o] <= endY);

solve minimize endY;

output [ "x-koordinates = \(startX)\nwidth = \(width)\ny-koordinates = \(startY)\nlength = \(endY)\n" ];

OBJECTS = {c1, c2, c3, c4, c5 };

dx = [3,3,5,5,1];
dy = [3,5,3,5,1];


width= 10;
%length = 50;

