To run files - 

python3 code.py alg file step

where

alg = "BT" for backtracking
alg = "MC" for minconflicts

file = .txt file

step =  0 for backtrack
step = num_steps for min conflicts


eg - 
backtrack - 
python3 code.py BT Sudoku_v2.txt 0

min conflicts - 
python3 code.py MC Map_v.txt 20


output - 

backtrack-

res_BT.txt - node_label assigned_val
Number of steps written to terminal


min conf-

res_MC.txt - node_label assigned_val
Number of steps written to terminal

