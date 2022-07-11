# VLSI Design Project 

## Contents
- Introduction
- Requirements
   - No rotation


 # Introduction
 This code is used for the Propositional SATisfiability models in our project in combinatorial
 decision making and optimization. We have one file.

 # Requirements
 To run the code you need to use a program compatible with python, we have used Spyder. You also need to install z-3 solver. 


 ## No Rotation
 SAT code: SATencoding.py
 Input code: ins-X.txt, X: the number of the instance

 The input-file needs to be of the following form and in .txt dataformat

 dx = array1d(1..n, [dx_1, .. , dx_n]);
 dy = array1d(1..n, [dy_1, .. , dy_n]);

 w = width of board;
 n = number of circuits;

 Our given files were of the following form in .txt, and we used the function "readfile" in SATencoding to create the needed format.

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
