import numpy as np
import collections
from collections import deque
import sys

def load_mat(fil):
	#load file
	mat = np.loadtxt(fil, dtype = np.str,delimiter=',')
	#replace 'G' to 0 for easier processing
	mat = np.char.replace (mat, 'G', '0')
	mat =mat.astype(int)
	row,col=np.shape(mat)

	#print matrix and (size of matrix)
	#print(mat)
	#print (row,col)

	#Preprocessing to create dict
	row=row-1
	col=col-1
	return row,col,mat


def create_graph_dfs(row,col):
	# Convert the grid to a dictionary 
	# dict => d[coordinates = (i,j)] = [accessible paths considering number of hops given in cell]
	# eg : d[(0,0)]: [(2,0),(0,2)]

	from collections import OrderedDict 
	d=OrderedDict()

	for i in range(row+1):
	    for j in range(col+1):
	        l=[]
	        v=mat[i][j]
	        if v != 0:
	            #move right
	            if (j+v)<=col:
	                l.append((i,j+v))

	            #move left
	            if (j-v)>=0:
	                l.append((i,j-v)) 
	            #move down
	            if (i+v)<=row:
	                l.append((i+v,j))   
	            #move up
	            if (i-v)>=0:
	                l.append((i-v,j))
	                        

	            #add to dict
	            d[(i,j)]=l
	        else:
	            #get goal coordinates
	            goal=(i,j)
	return d,goal 


def dfs(graph, first, goal, path=[]):
	#Add first to path
	path = path + [first]
	#use a global variable to count number of states
	global counter
	counter+=1
	#If goal node found, return
	if first == goal:
		return [path]
	#To store all paths
	paths = []
	for child in graph[first]:
		if child not in path:
			c_paths = dfs(graph, child, goal, path)
			for child_path in c_paths:
				paths.append(child_path)
	return paths



                
if __name__ == '__main__':
	fil = sys.argv[1]
	counter=0
	row,col,mat=load_mat(fil)
	graph,goal=create_graph_dfs(row,col)
	print ( " ---  DFS  ---")
	p=dfs(graph, (0,0), goal)
	print ("Number of unique paths : ",len(p))
	print ("The number of states expanded:",counter)



	
	
	

	


