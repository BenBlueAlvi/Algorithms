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

	print(queue)
	#while the queue isn't empty
	head = 0
	while head < len(queue):
		#pop
		u = queue[head]
		head += 1
		
		#add to output
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
	print(output)
	nValue = defaultdict(int)
	length = 0
	back = defaultdict(int)
	for u in output:
		for v in adjlist[u]:
			
			nValue[v] = max(nValue[v], nValue[u] + 1)
			
		back[nValue[u]] = u
	
	
	return (len(back) - 1 if len(back) > 0 else 0, list(back.values()))
	
print(longest(10, [(1, 2), (3, 4), (4, 6)])) #
print(longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])) #(5, [0, 2, 4, 3, 5, 6]) 
print(longest(100, [])) #(5, [0, 2, 3, 4, 5, 6])

	