from random import randint

#choose the ith smallest number in a
#best/avg O(n) ~ ith smallest is only on left side
#worst O(n^2) ~ ith smallest alternates between left and right sides, forcing the right side to be calaculated each time
def qselect(i, arr):
	if (i-1 < 0):
		print('Error: 0th smallest element')
		return
	if (i > len(arr)):
		print('Error: '+ str(i) + ' larger than array size')
		return
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
		
	
	
