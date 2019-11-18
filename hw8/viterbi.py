from collections import defaultdict

def longest(n, graph):
	adjlist = defaultdict(list)
	indegree = defaultdict(int)
	
	queue = []
	output = []
	conNodes = set()
	#O(E) set up adjlist and indgree list
	for u, v in graph:
		conNodes.add(u)
		conNodes.add(v)
		adjlist[u].append(v)
		indegree[v] += 1
	
	
	#add indgree 0s to queue
	for u in conNodes:
	
		if indegree[u] == 0:
			queue.append(u)
			

	#while the queue isn't empty
	head = 0
	while head < len(queue):
		#pop
		u = queue[head]
		head += 1
		
		
		output.append(u)
		
		#update indegrees
		
		for v in adjlist[u]:
			indegree[v] -= 1
			if indegree[v] == 0:
				#if an indegree becomes 0, add it to the queue
				queue.append(v)
		
	#check for if we didn't reach any nodes
	for u in range(n):

		if indegree[u] != 0:
			return None
	
	#begin VITERBI!
	
	
	nValue = defaultdict(int)
	
	back = defaultdict(int)
	rValue = defaultdict(int)
	for u in output:
		for v in adjlist[u]:
			
			nValue[v] = max(nValue[v], nValue[u] + 1)
			#backtrace reeeee
			
			if nValue[v] == nValue[u] + 1: back[v] = u
			rValue[nValue[v]] = v
			
	if (len(nValue) == 0): return (0, output)
	
	path = [rValue[max(rValue.keys())]]
	for i in range(len(rValue)):
		path.append(back[path[i]])
	
	path.reverse()
	return (len(rValue), path)
	

	