# VLSI Design Project 

## Contents
- Introduction
- Requirements
   - No rotation
   - Rotation

 # Introduction
 This code is used for the Mixed Integer Programming (MIP) models in our project in combinatorial
 decision making and optimization. We have two files, one for rotation and one without.

 # Requirements
 To run the code you need to use a program compatible with python, we have used Spyder. 
 You also need to download the Gurobi Optimizer. This can be done by this command
 ````
pip install gurobipy
````


 ## No Rotation
 MIP code: placeCircuitsLP.py
 Input code: insX.dzn, X:the number of the instance

 The input-file needs to be of the following form  
 
 w   
 n  
 dx_1 dy_1  
 ...  
 dx_n dy_n
 
 where dx_n and dy_n represents the width and length of the nth circuit

 The output will be of the format:  
 
 w  h  
 n  
 dx_1 dy_1 x_1 y_1  
 ...  
 dx_n dy_n x_n y_n
 
 And is written to an output file. 
 Where x_n and y_n are the koordinates where the rectangles are placed in the optimal solution, with the optimal height h.

 ## Rotation:
 MIP code: PlaceCircuits2Rotation.py
 Input code: insX.dzn, X:the number of the instance
 
 The input is in the same format as for no rotation:  
 
 w   
 n  
 dx_1 dy_1  
 ...  
 dx_n dy_n

 The output will be of the format:  
 
 w  h  
 n  
 dx_1 dy_1 x_1 y_1  
 ...  
 dx_n dy_n x_n y_n
 
 And is written to an output file. 
 Where x_n and y_n are the koordinates where the rectangles are placed in the optimal solution, with the optimal height h.
