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

		
	back = defaultdict(int)
	
	while (h != []):
		u = heappop(h)[1]
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
	for i in range(n-1):
		output.append(back[output[i]])
		
	output.reverse()
	return (len(output), output)

	