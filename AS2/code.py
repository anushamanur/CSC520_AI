import collections
import sys
import math
from random import randint

#read VARS from file and add to dictionary
def read_var(fil):
	with open(fil) as f:
		var=[]
		d=collections.OrderedDict()
		copy = False
		for line in f:
		    if line.strip() == "VARS":
		        copy = True
		    elif line.strip() == "ENDVARS":
		        copy = False
		    elif copy:
		        x=line.strip('\n').split(":")
		        d[x[0].strip()]=list(map(int, x[1].split()))
	return d
#read CONS from file and add to dictionary
def read_cons(fil):

	with open(fil) as f:
		
		d_cons=collections.OrderedDict()
		copy = False
		for line in f:
		    if line.strip() == "CONSTRAINTS":
		        copy = True
		    elif line.strip() == "ENDCONSTRAINTS":
		        copy = False
		    elif copy:
		        x=list(line.strip('\n').split("!="))
		        x=list(x[1].split())

		        for i in x:
		            for j in x:
		                if j!=i:
		                    if i not in d_cons:
		                        d_cons[i]=[j] 
		                    else:
		                        d_cons[i].append(j)
	return d_cons
#Generate matrix which considers constraints and creates an adjacency matrix                    
def gen_mat(d_cons):

	val = list(d_cons.keys())
	mat = [ [1 if x in v else 0 for x in val] for k, v in d_cons.items()]
	return mat,val

def backtrack(val,d,mat):

	# Python program for solution of M Coloring 
	# problem using backtracking 
	class Graph(): 

		def __init__(self, vertices,d,val): 
		    self.V = vertices   # number of nodes
		    self.Col=d          # Variable dependency
		    self.graph = [[0 for column in range(vertices)]for row in range(vertices)] 
		    self.val=val        #List of nodes
		    

		# A utility function to check if the assignment is safe for vertex v 
		def isSafe(self, v, colour, c): 
		    #For node v and its neighbours,  check all values
		    for i in range(self.V): 
		        #If any of its neighbours are already assigned that value, return False
		        if self.graph[v][i] == 1 and colour[i] == c: 
		            return False
		    return True

		
		def graphColourUtil(self, m, colour, v): 
		    global count
		    #If we have traversed all nodes, we have reached our solution
		    if v == len(self.Col): 
		        return True
		    
		    #Get domain values for that particular node
		    m=self.Col[self.val[v]]
		    
		    #Iterate through all domain values to see if any fit
		    for c in m: 
		        #Check if it safe to set a domain value at that particular position and node
		        if self.isSafe(v, colour, c) == True: 
		            #set value
		            colour[v] = c 
		            #Check for next node
		            if self.graphColourUtil(m, colour, v+1) == True: 
		                return True
		            #Could not find a safe assignment, backtrack
		            #backtrack and reinitialize colour to 0
		            colour[v] = 0
		            #increment counter to track number of backtracking steps
		            count+=1

		def graphColouring(self): #Driver function
		    #Initialize list to hold assigned values
		    colour = [0] * self.V 
		   
		    #Get domain values for node 0
		    m=self.Col[val[0]]
		    #Start with node 0
		    if self.graphColourUtil(m, colour, 0) == False: 
		        return False
		    print ("Number of steps :", count)
		    with open('res_BT.txt', 'w') as f:
    			for va,col in zip(self.val,colour):
        			f.write("%s " % va)
        			f.write("%s \n" % col)

		    return colour
        

	# Driver Code 
	g = Graph(len(val),d,val) 
	global count
	count =0
	g.graph = mat
	color=g.graphColouring() 


def min_conf(val,d,mat,stp):

	class Graph(): 

	    def __init__(self, vertices,d,val): 
	        self.V = vertices 
	        self.Col=d
	        self.graph = [[0 for column in range(vertices)]for row in range(vertices)] 
	        self.val=val
	
	    #find conflicts for for given node and value
	    def var_conflicts(self,v,colour,c):
	        var_conflicts = 0
	        for i in range(self.V): 
	            if self.graph[v][i] == 1 and colour[i] == c: 
	                var_conflicts+=1
	        return var_conflicts


	    #Returns overall conflict for the entire set of values over the list
	    def sudoku_conflicts(self,colour):
	        sum_conflicts = 0
	        for v in range(self.V):
	            sum_conflicts += self.var_conflicts(v,colour,colour[v])

	        return sum_conflicts


	    def search(self,graph, max_steps):
	        # Find fixed vars and randomize 
	        colour=[0] * self.V 
	        fixed_vars = set()
		#Randomize values within domain for initialization
	        for i,x in enumerate(val):
	            if len(self.Col[x])==1:
	                fixed_vars.add(i)
	                colour[i]=(self.Col[x])[0]
	            else:
	                l=len(self.Col[x])
	                colour[i] = randint(1, l)
	        

	        flag=0
	        i = 1
		#Run for max_steps
	        while i <= max_steps:
	            sum_conflicts = self.sudoku_conflicts(colour)
	            #If absolutely no conflict, return
	            if sum_conflicts == 0:
	                flag=1
	                return colour, i,flag

	            rand_x = randint(0, self.V-1)
	            #Pick random node

	            if rand_x in fixed_vars:
	                continue

	            m=self.Col[self.val[rand_x]]
	            #For domain of that node, find value with min conflict
	            for c in m:
	                if self.var_conflicts(rand_x,colour,colour[rand_x]) > self.var_conflicts(rand_x,colour,c):
	                    colour[rand_x] = c

	            i += 1

	        return colour, i,flag

	# Driver Code 
	g = Graph(len(val),d,val) 
	g.graph = mat
	max_steps=int(stp) 

	result, num_steps, converge = g.search(mat, max_steps)

	if converge ==1:
	    print(result)
	    print ("Number of steps taken :"  ,num_steps)
	    with open('res_MC.txt', 'w') as f:
    		for va,col in zip(val,result):
        		f.write("%s " % va)
        		f.write("%s \n" % col)
        	#f.write("Number of steps taken : %s" % num_steps)
        		
	else:
	    print("Did not converge!")

   
    



               

def BT(fil):
	d=read_var(fil)
	d_cons=read_cons(fil)
	mat,val=gen_mat(d_cons)
	res=backtrack(val,d,mat)
	return res
	

def MC(fil,stp):
	d=read_var(fil)
	d_cons=read_cons(fil)
	mat,val=gen_mat(d_cons)
	res=min_conf(val,d,mat,stp)
	return res


	
      

	





if __name__ == '__main__':

	alg = sys.argv[1]
	fil= sys.argv[2]
	max_step=sys.argv[3]

	if alg=="BT":
		res=BT(fil)
		
	if alg=="MC":
		res=MC(fil,max_step)
		
