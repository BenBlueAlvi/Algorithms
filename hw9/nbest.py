from heapq import heappush, heappop, heapify
def nbest(ABs):    # no need to pass in k or n
	k = len(ABs)
	n = len(ABs[0][0])
	def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
		A, B = ABs[i] # A_i, B_i
		if p < n and q < n and (i, p, q) not in used:
			heappush(h, (A[p] + B[q], i, p, q, (A[p],B[q])))
			used.add((i, p, q))
	h, used = [], set()                 # initialize
	for i in range(k):
		A, B = ABs[i]
		h.append((A[0] + B[0], i, 0, 0, (A[0], B[0])))
		used.add((i, 0, 0))
		
	heapify(h)
	
	for _ in range(n): 
		_, i, p, q, pair = heappop(h)
		yield pair     # return the next pair (in a lazy list)
		trypush(i, p + 1, q)
		trypush(i, p, q + 1)
print(list(nbest([([1,2,4], [2,3,5]), ([0,2,4], [3,4,5])]))) # [(0, 3), (1, 2), (0, 4)]