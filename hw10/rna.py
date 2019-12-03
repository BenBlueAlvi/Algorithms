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
	
	back = defaultdict(int)
	def _best(i, j):
		if (i, j) in OPT:
			return OPT[i, j]
			
		cur = 0
		for k in range(i, j):
			if _best(i,k) + _best(k+1, j) > cur:
				cur = _best(i,k) + _best(k+1, j)
				back[i, j] = k
				
		if x[i] + x[j] in pairs:		
			
			if _best(i+1, j-1) + 1 > cur:
				cur = _best(i+1, j-1) + 1
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
			return "(" + solution(i+1, j-1) + ")"
		else:
			print(k)
			return solution(i, k) + solution(k+1, j)
	
	OPT = defaultdict(int)
	
	#base cases
	for i in range(len(x)):
		OPT[i, i] = 0
		OPT[i, i-1] = 0
	b = _best(0, len(x)-1)
	print(back)
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






def kbest(x, k):
	back = defaultdict(list)
	
	def nbest(ABs, singleton, ijpairs):    
		
		
		
		
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
		
		for u in range(k):
			#print("heap:", h)
			if len(h) > 0:
				_, i, p, q, pair = heappop(h)
				
				if q == -1: #if we popped the singleton
					yield pair  
					#print("s", pair)
					trypush(i, p+1, q, True)
				else:
					back[ijpairs[i], u] = True
					
					yield pair 
					#print("q", pair)
					
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
		ijpairs = []
		for p in range(i, j):
			if x[p] + x[j] in pairs:
				
				squares.append((_kbest(i,p-1),_kbest(p+1, j-1)))
				ijpairs.append((p,j))
				
			
			
		if len(squares) > 0:
			#print(singleton)
			#print(squares)
			
			
			nb = list(nbest(squares, singleton, ijpairs))
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
	
	for i in range(k):
		print(solution(0, len(x), i))
	
	return b

		
print(best("ACAGU")) #().()
'''
(2, '((.))')
6
[(2, '((.))'), (1, 
 (1, '..(.)'), (1, '...()'), (1, '(...)'), (0, '.....')]
'''

#6

print(best("GCACG")) #[(2, '().()'), (1, '(..).'), (1, '()...'), (1, '.(..)'), (1, '...()'), (0, '.....')]
print(best("CCCGGG")) #[(3, '((()))'), (2, '((.)).'), (2, '(.()).'), (2, '.(()).'), (2, '.(().)'), (2, '.((.))'), (2, '((.).)'), (2, '(.(.))'), (2, '(.().)'), (2, '((..))')]
#print(kbest("UUGGACUUG", 129)) #().()
#print(best("CCGG")) #(())

	
	