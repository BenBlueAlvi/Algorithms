'''

	. -> A
	. -> G
	. -> U
	. -> C
	()
	

	mov eax, n - 5 + 1
	RandomRange() -> 0-n-1
	add eax, 5
	mov res, eax
	
'''


pairs = ["AU", "GU", "GC", "UA", "UG", "CG"]

def _best(seq, i, j, OPT = None):
	if OPT = None:
		i = 0
		j = len(seg) -1 
		OPT = [[-1 for _ in range(i)] for _ in range(j)]
	
	if OPT[i][j] == -1:
		if seq[i] + seq[j] in pairs:
			OPT[i][j] = OPT[i+1][j-1] + 1
		elif 
	else:
		OPT[i][j] = _best(seq, i, j, OPT) 
	
	
	
	