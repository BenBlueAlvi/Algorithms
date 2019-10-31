#like knapsack, but each item has c_i copies

'''
let's do 0-1 knapsack first
only 1 copy

Can convert to bounded by multiplying the copies as different elements

naive:
brute force it
2^n choices

DP:
Gotta keep track of which items have been used
Can't explicitly keep track of the store

max(add, not add)
max(n-1)

OPT(w)(if element was used or not) ~ best soltuion for bag of cap w withe items a[1] to a[i]

OPT(w)(i) ~ put i in or not?
OPT(w)(i) = max(OPT(w-i_w)(i-1) + i_v, OPT(w-1)(i))
					^take 			^no take
					
OPT[0][i] = 0
OPT[w][0] = 0

OPT is a 2d array
lower right is answer


space: O(nW)
Time: O(nW) ~ not polynomial in input size
'''

def best(max_weight, elements, OPT = None, i = None):
	if OPT is None:
		mElements = sum([[(i)]*i[2] for i in elements], [])
		OPT = [[0 for i in range(len(mElements)+1)] for j in range(max_weight+1)]
		
	
	for w in range(0, max_weight+1):
		for i in range(1, len(mElements)+1):
			
			if w >= mElements[i-1][0]:
				
				OPT[w][i] = max(OPT[w - mElements[i-1][0]][i-1] + mElements[i-1][1], OPT[w][i-1])
				
				
			else:
				
				OPT[w][i] =  OPT[w][i-1]
				
			
	
	#back trace this is all that's left
	'''selects = [0 for x in elements]

	i = 0
	j = 0
	while i < len(mElements):
		print(mElements[i][2])
		print(back[i:i+mElements[i][2]])
		selects[j] = sum(back[i:i+mElements[i][2]])
		i += mElements[i][2]
		j += 1
			
				
	print(sum([selects[i] * elements[i][1] for i in range(len(selects))]))'''
	
	selects = [0 for x in elements]
	w = max_weight
	for i in range(len(mElements), 0, -1):
		if OPT[w][i] != OPT[w][i-1]:
			selects[elements.index(mElements[i-1])] += 1
			w -= mElements[i-1][0]
	
	
	return (OPT[max_weight][len(mElements)], selects)
	

print(best(3, [(1, 5, 2), (1, 5, 3)])) #(15, [2, 1])
print(best(3, [(1, 5, 1), (1, 5, 3)])) #(15, [1, 2])
print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])) #(130, [6, 4, 1])
print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])) #(236, [6, 7, 3, 7, 2]) 
	