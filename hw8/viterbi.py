from collections import defaultdict

def longest(n, graph):
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
	
	#begin VITERBI!
	nValue = defaultdict(int)
	length = 0
	back = defaultdict(int)
	for u in output:
		for v in adjlist[u]:
			
			nValue[v] = max(nValue[v], nValue[u] + 1)
			
		back[nValue[u]] = u
	
	return (len(back)-1, list(back.values()))
	

	