import math

#tail recursion:
#single chain instead of branching

#T(n) = 2T(n/2) + O(n) + O(n) = 2T(n/2) + O(n) = O(nlogn)
#stable, along with insertion and non-random quicksort
#random quicksort, and default selection sort are not stable, but both can be made stable
def mergesort(arr):
	
	if (len(arr) > 1):
		#get midpoint
		mid =math.floor(len(arr) / 2)
		l = arr[:mid]
		r = arr[mid:]
		
		#deviding, O(logn)
		mergesort(l)
		mergesort(r)
		
		
		#merging, O(n)
		i = 0
		j = 0
		k = 0
		
	
		#place values in r and l back into arr based on whether or not one is greater than the other
		while j < len(r) and k < len(l):
			if r[j] < l[k]:
				arr[i] = r[j]
				j+=1
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
	
			
		
		
			
		
		
		
		
	return arr
	

	