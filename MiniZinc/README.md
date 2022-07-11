# VLSI Design Project 

## Contents
- Introduction
- Requirements
   - No rotation
   - Rotation

 # Introduction
 This code is used for the constraint programming models in our project in combinatorial
 decision making and optimization. We have two files, one for rotation and one without.

 # Requirements
 To run the code you need to use the program MiniZinc, and the solver configuration "Chuffed 0.10.4"


 ## No Rotation
 MiniZinc code: PlaceCircuitsSym.mzn
 Input code: insX.dzn, X:the number of the instance

 The input-file needs to be of the following form and in .dzn dataformat

 dx = array1d(1..n, [dx_1, .. , dx_n]);
 dy = array1d(1..n, [dy_1, .. , dy_n]);

 w = width of board;
 n = number of circuits;

 Our given files were of the following form in .txt, and we used the pythonscript "ConvertingToDzn.py" to create the needed format.

 w
 n
 dx_1 dy_1
 ...
 dx_n dy_n

 The output will be of the format:
 x-koordinates = [x_1, .. , x_n]
 width = with of board
 y-koordinates = [y_1, .. , y_n]
 height = optimal height
 
 Where x-koordinates and y-koordinates are the koordinates where the rectangles are placed in the optimal solution

 ## Rotation:
 MiniZinc code: PlaceCircuitsWithRotation.mzn
 Input code: insRotX.dzn, X:the number of the instance
 
 For the rotation inputfiles we needed an other format, using the pythonscript "ConvertingToDzn.py" to convert the filse. 
 The input-file needs to be of the following form and in .dzn dataformat


 rectOffsets = [|0,0,dx_1,dy_1| .. |0,0,dx_n,dy_n|];

 shape = array1d(1..2n, [{1}, .. , {2n}]);

 validshapes = array1d(1..n, [{1,2}, .. {2n-1,2n}]);

 dx = array1d(1..n, [dx_1, .. , dx_n]);

 dy = array1d(1..n, [dy_1, .. , dy_1]);

 w = width of the board;

 n = number of circuits;

 o = 2 * number of circuits;

 The output will be of the format:
 h = 8;
 x = [x_1, .. , x_n];
 y = [y_1, .. , y_n];
 kind = [k_1, .. , k_n];
 
 Where x and y are the koordinates where the rectangles are placed in the optimal solution
 Kind shows whether the rectangle is rotated or not. Even numbers mean it is rotated, while odd numbers are not rotated.
