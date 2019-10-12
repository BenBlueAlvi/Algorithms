from random import randint
'''

yeild - returns portion of function


quickselect problem

absolute value of arr - a
'''
def qselect(i, arr):
	#select a random pivot
	pivotIndex = randint(0, len(arr) - 1)
	pivot = arr[pivotIndex]
	
	#get left side
	left = [x for x in arr if x < pivot]
	
	#only recurse one side instead of 2, thus O(n)
	if (len(left) > i-1): #value is in left side
		return qselect(i, left)
	
	elif (len(left) < i-1): #value on right side
		#recurse on the right side
		right = [x for x in (arr[0:pivotIndex] + arr[pivotIndex+1:]) if x >= pivot]
		return qselect(i - len(left) - 1, right) #reduce i to fit within the bounds of the right side
	else:
		return pivot

#finds k closest numbers to a in arr
def find(arr, a, k):
	
	#get all the differences O(n)
	diffs = [abs(x - a) for x in arr]
	print(diffs)
	#find index of k smallest number in diffs O(n) [quickselect]
	sVal = qselect(k, diffs)
	print(sVal)
	
	
	#all numbers in diffs less than or equal to k should be printed
	#<
	closests = []
	for i in range(len(diffs)):
		if (diffs[i] < sVal):
			closests.append(arr[i])
			
		#scan twice, once for strictly smaller, second stricly equal 
		#=
		if (diffs[i] == sVal and len(closests) < k):
			closests.append(arr[i])
	
	
		
			
	#scan third time for printing numbers
	return closests



