from random import randint
#run to submit: flip $ /nfs/farm/classes/eecs/fall2019/cs325-001/submit hw1 qselect.py qsort.py report.txt

#best nlogn
#worst n^2 ` occurs when all numbers are sorted or reverse sorted and when pivoting around the first element
#basically when the tree created is extremely left or right heavy
def qsort(arr):
	#make sure array has stuff in it
	if (len(arr) == 0):
		return arr
		
	else:
		#height of created tree = log(n)
		#each layer of the tree is O(n)
		#thus the entire function is O(nlogn)
		
		#pivot around the first element
		#pivot = arr[0] <-- can cause worst case if sorted
		pivotIndex = randint(0, len(arr) - 1) # gotta know the index so we can exclude it later
		pivot = arr[pivotIndex] # random pivot greatly decreases the worst case senario
		
		#place everything smaller on left
		left = [x for x in arr if x < pivot] #O(n)
		#everything greater on right
		right = [x for x in (arr[0:pivotIndex] + arr[pivotIndex+1:]) if x >= pivot] #O(n), the equals sign here means we need to exclude the pivot so it isn't included multiple times
		#the equals sign can't be omited because elements equal to the pivot will not be included
		
		#recursivly sort left and right sides and place pivot in middle
		return [qsort(left)] + [pivot] + [qsort(right)] #wrapping brackets around the qsort calls here causes this function to return a BST representing the given array
	
	

#O(n) each node is hit once
def sorted(tree):
	return _sorted(tree, [])


	
def _sorted(tree, list):
	
	
	if (tree[0] != []):
		left = _sorted(tree[0], list)
	
	list.append(tree[1])
	
	if (tree[2] != []):
		right = _sorted(tree[2], list)
	return list
	
	
#O(n/2) ~ O(n) each time the algorithim selects one of two nodes to traverse
def insert(tree, value):
	#base case
	
	if (tree == []):
		tree = [[], value, []]
		return tree
	else:
		root = tree[1]
		if (value < root):
			#go left
			tree[0] = insert(tree[0], value)
			
		else:
			#go right
			tree[2] = insert(tree[2], value)
	
	return tree
	
#O(n/2) ~ O(n) each time the algorithim selects one of two nodes to traverse
def search(tree, value):
	#base case
	if (tree == []):
		return False
		
	root = tree[1]
	
	#value found
	if (root == value):
		return True
		
	elif (value < root):
		#go left
		return search(tree[0], value)
		
	else:
		#go right
		return search(tree[2], value)
		


tree = qsort([3, 5, 1, 2,3, 123, 32, 32, 43])
print(tree)
print(sorted(tree))
insert(tree, 20)
print("post insert")
print(tree)
print(search(tree, 1))
	