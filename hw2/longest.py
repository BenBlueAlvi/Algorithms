#similar to ninv
#return longest path and depth
#start and end in leaf nodes
#longest path, height +1


#check for O(n) time
	
def _longest(tree, clong):
	#if tree doesn't exist, return
	if (tree == []):
		return 0, clong

	#get left and right lengths
	llong, clong = _longest(tree[0], clong)
	rlong, clong = _longest(tree[2], clong)
	
	#check total length greater than current greatest length
	if (rlong + llong > clong):
		#if so, update current greatest length
		clong = rlong + llong
	
	#return the longer path in subtree +1 to include the starting node, and the current greatest length
	return 1 + max(rlong, llong), clong
	

def longest(tree):
	return _longest(tree, -1)[1]

	
	
