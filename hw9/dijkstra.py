from collections import defaultdict
from heapdict import heapdict

#use heapdict
#complexity: O(v) pops O(vlogv) time for pops: O((V+E)logV)
#space (O(V))
def shortest(n, edges):
	#set all values to +infinity, minus n
	values = defaultdict(lambda: float("inf"))
	
	values[0] = 0
	
	
	h = heapdict()
	h[0] = 0
	

	
	adjlist = defaultdict(list)
	for u, v, c in edges:
		adjlist[u].append((c, v))
		adjlist[v].append((c, u))

		
	back = defaultdict(int)
	visited = set()
	
	while (h):
		u = h.popitem()[0]
		
	
		if u in visited: continue
		visited.add(u)
		if u == n-1: break
		
		for c, v in adjlist[u]:
			if v in visited: continue
			values[v] = min(values[v], values[u] + c)
			
			if values[v] == values[u] + c: back[v] = u
			#print("v", v)
			
			h[v] = values[v]
				
		#print(h)
	if n-1 not in back: return None
	#backtrace
	output = [n-1]
	
	i = 0
	while (back[output[i]] != 0):
		output.append(back[output[i]])
		
		i += 1
	output.append(0)
	
	output.reverse()
	return (values[n-1], output)
