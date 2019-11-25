from collections import defaultdict
from heapq import heapify, heappop, heappush

#use heapdict
#complexity: O(v) pops O(vlogv) time for pops: O((V+E)logV)
#space (O(V))
def shortest(n, edges):
	#set all values to +infinity, minus n
	values = defaultdict(int)
	for i in range(1, n):
		values[i] = float("inf")
	values[0] = 0
	
	
	h = [(0,0)]
	

	
	adjlist = defaultdict(list)
	for u, v, c in edges:
		adjlist[u].append((c, v))
		adjlist[v].append((c, u))

		
	back = defaultdict(int)
	visited = set()
	
	while (h != []):
		u = heappop(h)[1]
		
	
		
		if u in visited: continue
		visited.add(u)
		if u == n-1: break
		
		for c, v in adjlist[u]:
			values[v] = min(values[v], values[u] + c)
			
			if values[v] == values[u] + c: back[v] = u
			#print("v", v)
			#decrease key
			if v not in h:
				heappush(h, (values[v], v))
				
			else:
				for k in range(len(h)):
					if h[k][1] == v:
						h[k][0] = values[v]
						break
				heapify(h)
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
	return (len(output), output)
print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])) #None
print(shortest(8, [(0,4,2),(0,1,7),(0,7,12),(1,2,1),(1,3,1),(1,7,5),(2,3,3),(2,4,1),(2,5,1),(2,7,10),(3,6,2),(3,4,5),(3,7,1)]))
#(6, [0, 4, 2, 1, 3, 7])