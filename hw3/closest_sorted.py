

def _bisearch(arr, v):

	#non recursive search (because why not?)
	l = 0
	r = len(arr)
	#make sure l and r are within bounds
	while (l <= r and r <= len(arr)):	
		#get mid
		mid = (l+r)//2
		#make sure mid stays within bounds
		if (mid >= len(arr) or mid < 0):
			#subtract 1 to keep in bounds, this is due to how integer division works
			mid -= 1
			break
			
		#move left
		if (arr[mid] < v):
			l = mid + 1
		#move right
		
		elif(arr[mid] > v):
			r = mid - 1
			
		else:
			return mid
		
		
			
	return mid
	




def find(arr, a, k):

	#special cases for if a is outside array
	if (arr[0] >= a): return arr[:k]
	if (arr[len(arr)-1] <= a): return arr[-k:]
	

	#use binary search to get index of closest number
	#O(logn)
	idx = _bisearch(arr, a)
	

	
	#use double pointers to traverse through array forwards and backwards
	i = idx
	j = idx
	
	print(idx)
	
	#go thorugh k values, i traverses backward, j traverses forward
	#O(k)
	#there's another case in here we need to test, which side is closer
	while (k > 0):
		#only calculate diff is j within in the array
		if (j < len(arr)): 
			diff = abs(arr[i] - a) < abs(arr[j] - a) 
			#special case for the beginnning
			if (i == idx and j == idx): diff = True 
		else: 
			#otherwise just move i
			diff = True
		
		#process earlier values first
		if (diff and i > 0): #check to make sure we are in bounds
			k -= 1
			i -= 1
			
			
		#process later values second
		if (k > 0 and not diff and j < len(arr) or i == 0): #check to make sure we haven't run out of ks and are in bounds
			k -= 1
			j += 1
			
			
		
		
		
		
	return arr[i:j]
	
	

	
print(find([1,2,3,4,4,5,6], 3.3, 4)) #returns   [2, 3, 4, 4]
print(find([1,2,3,4,4,6,6], 5, 3)) #returns   [4,4,6]
	