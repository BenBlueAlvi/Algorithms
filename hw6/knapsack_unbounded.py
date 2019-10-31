'''

Weighted bag elements

weight w_i and v_i

can be copies

if bag has max weight of 3, 

returns best, and [copies of 1, copies of 2] etc...



'''

#greedy
'''
Every item, calculate v_i / w_i = average vaulue per weight.
choose the one with heighest average value per weight that fits
^doesn't work because it doesn't take into account the max_weight of the bag

Counter example:
(2, 4) and (3, 5) in bag of 3
AVW = 2, 1.6
First is better so add
Bag no longer has any space, max value is 4, which is inccorect

Define DP sub problem:
Optimization problem: OPT of w ~ best solution (max total value) for a bag of capacity w

Orginal problem is OPT of W

Recursive relations:
As long as the item fits
Look at each item and find the best one
OPT[w] = OPT(w-weight of item added) + value of item added ~ choose best item over max i to n
or
OPT(w-1) + 0 (dont' add an item)

max(OPT(w-weight of item added) + value of item added, OPT(w-1))

make sure bag is big enough to fit item
max([x for i in elements if w >= x.w])

Base case all remaining weights greater than remaining weight in bag
ie
{0: 0}
OPT(w) = 0 if w < smallest item wieght

Space O(w)
'''
#Complexity O(w), for each subproblem O(n) work is done, do it's O(w*n)
def best(max_weight, elements, prev = None):
	if prev is None:
		prev = {0 : (0, [0 for i in elements], 0)}
	print("W", max_weight)
	if max_weight not in prev:
		
		#a is previous bests
		a = [(best(max_weight-x[0], elements, prev), x) for x in elements if max_weight >= x[0]]
		an = [(x[0][0] + x[1][1], a) for x in a]
		#print(a)
		if a == []:
			prev[max_weight] = (0, [0 for i in elements], max_weight)
			print("FAIL")
		else:
			
			b = max(an) 
			#get results for adding b and not adding b
	
			add, noAdd = b[0], best(max_weight-1, elements, prev)
			print("A", add)
			print("N", noAdd)
			
			maxVal = max(noAdd[0], add)
			
			if (maxVal == add):
				#update new solution with maxVal, and previous solution + the new val
				print(b[1][0][0][1])
				print(b[1][0][1])
				n = [x for x in b[1][0][0][1]]
				n[elements.index(b[1][0][1])] += 1 
				print(max_weight)
				print((maxVal, max_weight))
				prev[max_weight] = (maxVal, noAdd[1], max_weight)
			else:
				print('NO ADD')#<--- issue here is this never runs. Ever
				#print(max_weight)
				#print((maxVal, noAdd[1]))
				prev[max_weight] = (maxVal, noAdd[1], max_weight)
			#print(b)
			
		
	
	return prev[max_weight]
	



#print(best(3, [(1, 5), (1, 5)])) #(15, [3, 0])
#print(best(3, [(1, 2), (1, 5)])) #(15, [0, 3])
#print(best(3, [(1, 2), (2, 5)])) #(7, [1, 1])
print(best(58, [(5, 9), (9, 18), (6, 12)])) #21, [1, 0, 1] #(114, [2, 4, 2])
#print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)])) #(109, [1, 1, 7, 1])