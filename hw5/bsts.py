#number of n-node BSTS

#0: empty node

#Qa: O(nlogn) ~ n * T(n) + T(n-1)

#Qb: Catalan Numbers

def bsts(n, n_bsts = None):
	if n_bsts is None:
		n_bsts = {0 : 1, 1 : 1}
	if n not in n_bsts:
		#split left and right trees, decide root left: (1 to i-1) right: (i+1 to n)
		#choices between left and right multiply
		
		#do over all is from 1 to n
		x = 0 
		for i in range(n):
			x += bsts(i) * bsts(n-(i+1))
		n_bsts[n] = x
	return n_bsts[n]
	
print(bsts(2)) #2
print(bsts(3)) #5
print(bsts(4)) #42
print(bsts(5)) #42

print(bsts(6)) #42
	
	