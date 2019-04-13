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

def create_graph(row,col):
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
	            #move up
	            if (i-v)>=0:
	                l.append((i-v,j))
	            #move down
	            if (i+v)<=row:
	                l.append((i+v,j))
	            #move left
	            if (j-v)>=0:
	                l.append((i,j-v))
	            #move right
	            if (j+v)<=col:
	                l.append((i,j+v))
	            #add to dict
	            d[(i,j)]=l
	        else:
	            #get goal coordinates
	            goal=(i,j)
	return d,goal

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


def bfs(graph, goal, first):
    """
    BFS is breadth first search which takes in 3 param: graph , goal state, initial state
    If path found : return path
    else : returns None
    """
    count=0
    #If initial state is itself the goal state, return first else add to queue and mark visited
    if first == goal:
        return [first]
    
    #Use Q to keep track of current state and path and initialize with first state
    que = deque([(first, [])])
    
    #mark visited
    visit_yes = {first}
    
    
    #while q is non-empty - ( FIFO structure)
    while len(que)!=0:  
        
        #get current state and path
        current_node= que.popleft()
        #Get current node and mark as visited
        cur=current_node[0]
        visit_yes.add(cur)
        count+=1
        
        #get path
        path=current_node[1]
                
        
        #Iterate through children of current node ( a.k.a neighbours)
        for child in graph[cur]:
            
            # For each check if it goal, if yes, return path
            if child == goal:
                return path + [cur, child],count
            
            #If child has already been visited, continue with next child
            elif child in visit_yes:
                continue
            
            #else, mark as visited and append child to queue with path from current state
            visit_yes.add(child)  
            
            que.append((child, path + [cur]))
 
    # path not found
    return None 



def dfs(graph, goal, first):
    #We use a LIFO structure for DFS
    
    #Use a set to store visited nodes
    visit_yes= set()
    count =0
    #Initialize stack with cuurent node and path
    lifo = [(first, [first])]
    
    #While stack is non empty
    while len(lifo)!=0:
        
        #Pop node off stack
        current_node = lifo.pop()
        count+=1
        #get coordinates of current node
        cur=current_node[0]
        
        #Get path to current path
        path=current_node[1]
        
        if cur not in visit_yes:
            #If goal node is found, return path
            if cur == goal:
                return path,count
            
            else:
                #Add all its children to stack
                for child in graph[cur]:
                    lifo.append((child, path + [child]))
                
                #mark current node as visited
                visit_yes.add(cur)
    # path not found
    return None

class Node():
    #Use node to store current position of traversal
    #Use node to store its parent node info to trace path

    def __init__(self, parent=None, curr=None):

        self.g = self.h = self.f = 0
        self.parent = parent
        self.cur_pos = curr


    
def astar(graph, goal, first):
    

    # initialize goal node and set parent to none
    end_node = Node(None, goal)
    end_node.h = 0
    end_node.f = 0
    end_node.g = 0
    
    # initialize first node and set parent to none    
    first_node = Node(None, first)
    first_node.h = 0
    first_node.f = 0
    first_node.g = 0

    # Initialize lists
    li = []
    final_list = []

    # Add first node to list
    li.append(first_node)
    c=0  
      
    # Loop until you find the end
    while len(li)!=0:

        # Get the first node in list
        cur_node = li[0]
        cur_ind = 0
        
        #Loop to find lowest F cost cell in li.
        for ind, node in enumerate(li):
            if node.f < cur_node.f:
                #get node and index
                cur_ind = ind
                cur_node = node
                
        
        # Pop current node off li, add to final list
        li.pop(cur_ind)
        c+=1
        final_list.append(cur_node)
        
        # Found the goal
        if cur_node.cur_pos == end_node.cur_pos:
            path = []            
            
            current = cur_node
            while current is not None:
                
                path.append(current.cur_pos)
                current = current.parent
            return path[::-1], c # Return reversed path 

        
        # Generate children
        children = []
        
        for node in graph[cur_node.cur_pos]: # Adjacent squares
                                
            # Create new node
            new_node = Node(cur_node, node)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # If child is already in final list, continue to next child 
            for final_child in final_list:
                if child == final_child:
                    continue

            # Calculate the f, g, and h values
            
            #heurisitc function
            #h(n) rules
            # If child is in the same row OR column as the goal then h=1
            # If it is in a different row and column then h=2.
            
            #Calculate h
            dx=abs(child.cur_pos[0] - end_node.cur_pos[0]) 
            dy=abs(child.cur_pos[1] - end_node.cur_pos[1])
            if dx==0 or dy==0:
                h=1
            else:
                h=2
            child.h =  h
            
            child.g = cur_node.g + 1
            child.f = child.g + child.h

            # If child is already in li 
            for node in li:
                #If child is in li or doesnt have a lesser g value indicating a abetter path, 
                #continue to next child
                if child == node and child.g > node.g:
                    continue

            # If child is not in li, or as checked above has a lesser g value, add the child to li
            li.append(child)
            
    # path not found
    return None


    
def greedy_bfs(graph, goal, first):
    

    # initialize goal node and set parent to none
    end_node = Node(None, goal)
    end_node.h = 0
    end_node.f = 0
    end_node.g = 0
    
    # initialize first node and set parent to none    
    first_node = Node(None, first)
    first_node.h = 0
    first_node.f = 0
    first_node.g = 0

    # Initialize lists
    li = []
    final_list = []

    # Add first node to list
    li.append(first_node)
    count=0  
      
    # Loop until you find the end
    while len(li)!=0:

        # Get the first node in list
        cur_node = li[0]
        cur_ind = 0
        
        #Loop to find lowest F cost cell in li.
        for ind, node in enumerate(li):
            if node.f < cur_node.f:
                #get node and index
                cur_ind = ind
                cur_node = node
                
        
        # Pop current node off li, add to final list
        li.pop(cur_ind)
        count+=1
        final_list.append(cur_node)
        
        # Found the goal
        if cur_node.cur_pos == end_node.cur_pos:
            path = []            
            
            current = cur_node
            while current is not None:
                
                path.append(current.cur_pos)
                current = current.parent
            return path[::-1], count # Return reversed path 

        
        # Generate children
        children = []
        
        for node in graph[cur_node.cur_pos]: # Adjacent squares
                                
            # Create new node
            new_node = Node(cur_node, node)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # If child is already in final list, continue to next child 
            for final_child in final_list:
                if child == final_child:
                    continue

            # Calculate the f, g, and h values
            
            #heurisitc function
            #h(n) rules
            # If child is in the same row OR column as the goal then h=1
            # If it is in a different row and column then h=2.
            
            #Calculate h
            dx=abs(child.cur_pos[0] - end_node.cur_pos[0]) 
            dy=abs(child.cur_pos[1] - end_node.cur_pos[1])
            if dx==0 or dy==0:
                h=1
            else:
                h=2
            child.h =  h
            
            child.g = cur_node.g 
            child.f = child.g + child.h

            
            if child not in li :#and child.g > node.g:
                li.append(child)
            
    # path not found
    return None




if __name__ == '__main__':

	alg = sys.argv[1]
	fil= sys.argv[2]
	print(alg)

	if alg=="BFS":
		row,col,mat=load_mat(fil)
		graph,goal=create_graph(row,col)
		path,count = bfs(graph, goal, (0,0))
		print ( " ---  BFS  ---")
		if path:
        		print("Shortest path - ", path)
        		print ("Number of states : ", count)
		else:
        		print('OOPS!! Path not found!')
		print("---")

	if(alg=="DFS"):
		row,col,mat=load_mat(fil)
		graph,goal=create_graph_dfs(row,col)
		path,count = dfs(graph, goal, (0,0))
		print ( " ---  DFS  ---")

		if path:
        		print("Path - ", path)
        		print ("Number of states : ", count)
		else:
        		print('OOPS!! Path not found!')
		print ("---")
	if alg=="Astar":
		row,col,mat=load_mat(fil)
		graph,goal=create_graph(row,col)
		path,count = astar(graph, goal, (0,0))

		print ( " ---  Astar  ---")

		if path:
        		print("Shortest path - ", path)
        		print ("Number of states : ", count)
		else:
        		print('OOPS!! Path not found!')

		print ("---")
	if alg=="BestFirst":
		
		row,col,mat=load_mat(fil)
		graph,goal=create_graph(row,col)
		path,count = greedy_bfs(graph, goal, (0,0))
		print ( " ---  Greedy best first search  ---")

		if path:
        		print("Shortest path - ", path)
        		print ("Number of states : ", count)
		else:
        		print('OOPS!! Path not found!')
        
