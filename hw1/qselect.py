from random import randint

#choose the ith smallest number in a
#best/avg O(n) ~ ith smallest is only on 
#worst O(n^2)
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
		
	
	
print(qselect(3, [5, 3, 1, 10, 12, 4]))