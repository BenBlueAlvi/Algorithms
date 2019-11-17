from heapq import heappush, heappop, heapify
from collections import defaultdict

#O(EV) ~ may be too slow
def order(n, graph):
	#in-degree, value
	#should be per node instead of edge
	nodes = [[0, i, []] for i in range(n)] #O(V)
	
	'''
	convert to adjecentcy list
	ie, one list for one node, list of edges from that node
	'''
	
	
		
		
		
	
	#for all nodes
	for i in range(n): #O(V)
		
		#for every edge
		for j in range(len(graph)): #O(E)
			
			#if some other node has an edge to this node
			if (i ==  graph[j][1]):
				#increase the in-degree of this node by 1
				nodes[i][0]+=1
				
			#add go to verts
			if (i == graph[j][0]):
				nodes[i][2].append(graph[j][1])
				
	print(nodes)
	#create heap possible nodes
	
	heapify(nodes) #O(V)
	
	print(nodes)
	output = []
	while nodes != []:
		#get val with in-degree 0'
		
		#v is current node
		v = heappop(nodes) #O(logV)
		
		print("v:", v)
		#check for loops
		if v[0] == 1:
			return None
		
		for i in range(len(v[2])): #O()
			#if the v goes to any vert in g
			
			for j in range(len(nodes)): #O(V)
				if nodes[j][1] == v[2][i]:
					nodes[j][0] -= 1
		

		
		pushed = False
		#update g
	
		
		
		
		
		output.append(v[1])
	return output
	
def order2(n, graph):
	adjlist = defaultdict(list)
	indegree = defaultdict(int)
	
	stack = []
	output = []
	#O(E) set up adjlist and indgree list
	for u, v in graph:
		adjlist[u].append(v)
		indegree[v] += 1
	
	#add indgree 0s to stack
	for u in range(n):
	
		if indegree[u] == 0:
			stack.append(u)
	
	#while the stack isn't empty
	head = 0
	while head < len(stack):
		#pop
		u = stack[head]
		head += 1
		
		#add to output
		output.append(u)
		
		#update indegrees
		for v in adjlist[u]:
			indegree[v] -= 1
			if indegree[v] == 0:
				#if an indegree becomes 0, add it to the stack
				stack.append(v)
				
	#check for if we didn't reach any nodes
	for u in range(n):

		if indegree[u] != 0:
			return None
	
	return output
	


print(order2(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])) #[0, 1, 2, 3, 4, 5, 6, 7]
print(order2(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])) #[0, 1, 2, 4, 3, 5, 6, 7]
print(order2(4, [(0,1), (1,2), (2,1), (2,3)])) #None
print(order2(5, [(0,1), (1,2), (2,3), (3,4)])) # [0, 1, 2, 3, 4]
print(order2(1, [(0,0)]))
print(order2(3, [(1,2), (2,1)]))
print(order2(5, []))
