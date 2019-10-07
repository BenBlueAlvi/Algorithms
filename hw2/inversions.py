import math
#how many pairs in the opposite order
#if sorted, 0
#reverse sorted, n(n-1)/2
#3, 1, 5, 2, 4 = 4
#should be nlogn
#equal to number of sort swaps
#if left pointer less than right, no inversions
def num_inversions(arr, ninv):

	if (len(arr) > 1):
		#get midpoint
		mid =math.floor(len(arr) / 2)
		l = arr[:mid]
		r = arr[mid:]
		
		#deviding, O(logn)
		ninv = num_inversions(l, ninv)[1]
		ninv = num_inversions(r, ninv)[1]
		
		
		#merging, O(n)
		i = 0
		j = 0
		k = 0
		
		#place values in r and l back into arr based on whether or not one is greater than the other
		while j < len(r) and k < len(l):
			if r[j] < l[k]:
				arr[i] = r[j]
				j+=1
				ninv += 1
			else:
				arr[i] = l[k]
				k+=1
			i+=1
			
		#place any leftover values in. Only one of these two while loops will be called
		while j < len(r):
			arr[i] = r[j]
			i+=1
			j+=1
			
		while k < len(l):
			arr[i] = l[k]
			i+=1
			k+=1
			
		
		
			
		
		
		
		
	return arr, ninv
				
print(num_inversions([4, 1, 3, 2], 0)) #4
print(num_inversions([2, 4, 1, 3], 0)) #3
		