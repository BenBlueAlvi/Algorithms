'''

	. -> A
	. -> G
	. -> U
	. -> C
	()
	

'''
from collections import defaultdict
from heapq import heapify, heappop, heappush

pairs = set(["AU", "GU", "GC", "UA", "UG", "CG"])

#profs
#complete but slow
def best(x):
	
	back = {}
	def _best(i, j):
		if (i, j) in OPT:
			return OPT[i, j]
			
		cur = -1
		for k in range(i, j):
			if x[k] + x[j] in pairs:	
				if _best(i,k-1) + _best(k+1, j-1) + 1 > cur:
					cur = _best(i,k-1) + _best(k+1, j-1) + 1
					
					back[i, j] = k
				
			
			
		if _best(i, j-1) > cur:
			cur = _best(i, j-1)
			back[i, j] = -1

		OPT[i, j] = cur
		return OPT[i, j]

	
	def solution(i, j):
		if i == j:
			return "."
		if i > j:
			return ""
		k = back[i, j]
		if k == -1:
			return solution(i, j-1) + "."
		
		else:
			return solution(i, k-1) + "(" + solution(k+1, j-1) + ")"
	
	OPT = defaultdict(int)
	
	#base cases
	for i in range(len(x)):
		OPT[i, i] = 0
		OPT[i, i-1] = 0
	b = _best(0, len(x)-1)
	
	return b, solution(0, len(x)-1)


#Complete!
def total(x):
	
	
	def _total(i, j):
		if (i, j) in OPT:
			return OPT[i, j]
			
		cur = 0
		
		cur += _total(i, j-1)	
			
		for k in range(i, j):
			if x[k] + x[j] in pairs:
				cur += _total(i,k-1) * _total(k+1, j-1)
			

		OPT[i, j] = cur
		return OPT[i, j]
	OPT = defaultdict(int)
	
	for i in range(len(x)):
		OPT[i, i] = 1
		OPT[i, i-1] = 1
	
	return _total(0, len(x)-1)





#another, more complex and broken, version that almost works
def kb(x, k):
	back = defaultdict(int)
	usedKs = set()
	def nbest(ABs, singleton, ijpairs, spair):    
		
		def trypush(i, p, q, isSingleton):  # push pair (A_i,p, B_i,q) if possible
			if isSingleton:
				if p < len(singleton) and not (i,p,q) in used:
					heappush(h, (-singleton[p], i, p, q, (singleton[p])))
					used.add((i, p, q))
					
			else:
				A, B = ABs[i] # A_i, B_i
				#print("AB: ", A, B, p, q)
				if p < len(A) and q < len(B) and not (i,p,q) in used:
					heappush(h, (-(A[p]+B[q]+1), i, p, q, (A[p] + B[q]+1)))
					used.add((i, p, q))

		h, used = [], set() # initialize
	
		h = [(-(A[0]+B[0]+1), i, 0, 0, (A[0]+B[0]+1)) for i, (A,B) in enumerate(ABs)] # add 1 for the pair
		h.append((-singleton[0], 0, 0, -1, (singleton[0])))
		heapify(h)
		last = ijpairs[0]
		for u in range(k):
			#print("heap:", h)
			if len(h) > 0:
				_, i, p, q, pair = heappop(h)
				
				if q == -1: #if we popped the singleton
				
					yield pair 
					
					#print("s", pair)
					trypush(i, p+1, q, True)
				else:
					if u in usedKs:
						
						back[ijpairs[i], u] = True
					
					back[ijpairs[i], u] = True
					usedKs.add(u)
					last = ijpairs[i]
					yield pair
					
					
					
					
					trypush(i, p, q+1, False)
					trypush(i, p+1, q, False)
		
	def solution(i, j, u):
		sol = ["." for _ in range(len(x))]
		for l in range(i, j):
			for v in range(l+1, j):
				
				if back[(l, v), u]:
					sol[l] = "("
					sol[v] = ")"
			
		fin = ""
		for e in sol:
			fin += e
		return fin

	def _kbest(i, j):
		if (i, j) in OPT:
			return OPT[i, j]
			
		cur = []
		squares = []
	
		singleton = _kbest(i, j-1)	
		spair = (i, j-1)
		ijpairs = []
		for p in range(i, j):
			if x[p] + x[j] in pairs:
				
				squares.append((_kbest(i,p-1),_kbest(p+1, j-1)))
				ijpairs.append((p,j))
				
			
			
		if len(squares) > 0:
			#print(singleton)
			#print(squares)
			
			
			nb = list(nbest(squares, singleton, ijpairs, spair))
			OPT[i, j] = nb
			
		
			
			#print(OPT[i, j])
		else:
			OPT[i, j] = singleton
		
		return OPT[i, j]
	



	OPT = defaultdict(list)
	
	
	for i in range(len(x)):
		OPT[i, i] = [0]
		OPT[i, i-1] = [0]
		
	b = _kbest(0, len(x)-1)
	print(back)
	for p in range(k):
		
		print(solution(0, len(x), p))
	
	
	return b
	
def kbest(x, k):
	
	topk = defaultdict(list)
	def _kb(i, j):
		def trypush_b(s, p, q):
			if (s, p, q) not in visited and p < len(topk[i,s-1]) and q < len(topk[s+1, j-1]):
				heappush(h, (-(topk[i,s-1][p][0] + topk[s+1,j-1][q][0] + 1), (s, p, q)))
				visited.add((s, p, q))
		def trypush_s(p):
			if p < len(topk[i, j-1]):
				heappush(h, (-(topk[i, j-1][p][0]), (p,)))
				
		if (i,j) in topk:
			return topk
			
		h = []
		visited = set()
		
		_kb(i, j-1)
		h.append((-(topk[i, j-1][0][0]), (0,)))
			
		
		for s in range(i, j):
			if x[s] + x[j] in pairs:
				_kb(i, s-1)
				_kb(s+1, j-1)
				
				h.append((-(topk[i,s-1][0][0] + topk[s+1,j-1][0][0] + 1), (s, 0, 0)))
		heapify(h)	
		for _ in range(k):
			if len(h) > 0:
				score, indices = heappop(h)
				score = -score
				
				if len(indices) == 1: #singleton
					p = indices[0]
					
					topk[i,j].append((score, topk[i,j-1][p][1] + "."))
					trypush_s(p+1)
				else:
					s, p, q = indices
					topk[i,j].append((score, topk[i,s-1][p][1] + "(" + topk[s+1,j-1][q][1] + ")"))
					trypush_b(s, p+1, q)
					trypush_b(s, p, q+1)
				
	
	
	for i in range(len(x)):
		topk[i,i] = [(0, ".")]
		topk[i, i-1] = [(0, "")]
	_kb(0, len(x)-1)	
	return topk[0, len(x)-1]
		
#print(kbest("ACAGU", 6)) #().()
'''
(2, '((.))')
6
[(2, '((.))'), (1, 
 (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]
'''

#6

print(best("GCACG")) #[(2, '().()'), (1, '(..).'), (1, '()...'), (1, '.(..)'), (1, '...()'), (0, '.....')]
#print(kb("CCCGGG", 6)) #[(3, '((()))'), (2, '((.)).'), (2, '(.()).'), (2, '.(()).'), (2, '.(().)'), (2, '.((.))'), (2, '((.).)'), (2, '(.(.))'), (2, '(.().)'), (2, '((..))')]
#print(kbest("UUGGACUUG", 129)) #().()
#print(best("CCGG")) #(())

	
	