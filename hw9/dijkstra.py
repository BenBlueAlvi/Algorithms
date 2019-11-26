from collections import defaultdict
from heapdict import heapdict

#use heapdict
#complexity: O(v) pops O(vlogv) time for pops: O((V+E)logV)
#space (O(V))
def shortest(n, edges):

	#set all values to +infinity, minus n
	values = defaultdict(lambda: 10000)
	
	values[0] = 0

	h = heapdict()
	h[0] = 0
	
	adjlist = defaultdict(list)
	for u, v, c in edges:
		adjlist[u].append((c, v))
		adjlist[v].append((c, u))

		
	back = defaultdict(int)
	visited = set()
	
	def backtrace(v):
		#base case if we reach 0
		if v not in back: return [v]
		return backtrace(back[v]) + [v]
	
	while (len(h) > 0):
		u = h.popitem()[0]
		
		if u == n-1: break
		if u in visited: continue
		visited.add(u)
		
		
		for c, v in adjlist[u]:
			
			if v in visited: continue
			values[v] = min(values[v], values[u] + c)
			
			if values[v] == values[u] + c: back[v] = u
			if v == n-1: break
			if v in h:
				if h[v] != values[v] : h[v] = values[v]
			else:
				 h[v] = values[v]
			#print("v", v)	
				
		#print(h)
	if n-1 not in back: return None
	#backtrace

	return (values[n-1], backtrace(n-1))
	
	
	
print(shortest(5, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])) #None
print(shortest(8, [(0,4,2),(0,1,7),(0,7,12),(1,2,1),(1,3,1),(1,7,5),(2,3,3),(2,4,1),(2,5,1),(2,7,10),(3,6,2),(3,4,5),(3,7,1)]))
#(6, [0, 4, 2, 1, 3, 7])
print(shortest(1000, [(0, 89, 10), (0, 221, 5), (0, 301, 20), (0, 331, 5), (0, 404, 16), (0, 728, 21), (0, 999, 27), (89, 451, 10), (89, 605, 5), (89, 728, 11), (89, 999, 16), (221, 236, 10), (221, 268, 9), (221, 382, 5), (221, 331, 5), (301, 331, 7), (301, 728, 8), (301, 999, 15), (331, 404, 7), (331, 473, 8), (331, 496, 10), (332, 534, 10), (331, 999, 30), (728, 996, 9), (996, 999, 5), (728, 999, 5)])) 
# should return something like (25, [0, 331, 301, 728, 999])