from random import randint
import heapq #<-- study heap insert remove etc
#quiz 2: code fill in the blanks
#python statement, complexity

#amortized: stardized complexity, ex: list.append(1) mostly O(1), but if list must resize O(n)

#python delete resizes arrays on deletes too, again by half
#will be on midterm

#log n, can be improved to 1
def bubble_up(arr, idx):
	if (arr[idx] < arr[idx//2]):
		arr[idx], arr[idx//2] = arr[idx//2], arr[idx]
		bubble_up(arr, idx//2)

def heap_insert(arr, val):
	arr.append(val)
	idx = len(arr)-1
	bubble_up(arr, idx)
	
#log n
def bubble_down(arr, idx):
	if (idx * 2 < len(arr) and idx*2 + 1 < len(arr)):
		#left child less
		if (arr[idx*2] < arr[idx*2+1]):
			arr[idx], arr[idx*2] = arr[idx*2], arr[idx]
			bubble_down(arr, idx*2)
		else:
			arr[idx], arr[idx*2+1] = arr[idx*2+1], arr[idx]
			bubble_down(arr, idx*2+1)
	elif(idx * 2 < len(arr)):
		arr[idx], arr[idx*2] = arr[idx*2], arr[idx]
		bubble_down(arr, idx*2)
	else:
		return
		
	



def paircomp(p1, p2):
	return p1[0] + p1[1] < p2[0] + p2[1] or (p1[0] + p1[1] == p2[0] + p2[1] and p1[1] < p2[1])

def qsort(arr):
	if (arr == []): return []
	pivot = arr[0]
	left = [x for x in arr if paircomp(x, pivot)]
	right = [x for x in arr if not paircomp(x, pivot)]
	return left + right
	

#returns top n of AxB = { (x, y) | x in A, y in B }

#O(2n^2 + logn)
def nbesta(a, b):
	best = []
	n = len(a)
	#enumerate
	for x in a:
		for y in b:
			best.append((x,y))
	#sort	
	print(best)
	best = qsort(best)
	
	#return top n
	return best[:n]
	

#this returns the k smallest values of arr	
def qselects(arr, k):
	
	pivotIdx = randint(0, len(arr)-1)
	pivot = arr[pivotIdx]
	
	left = [x for x in arr if paircomp(x, pivot)]
	
	if (len(left) > k):
		
		return qselects(left, k)
	
	elif (len(left) < k):
		
		right = [x for x in arr if not paircomp(x, pivot)]
		
		return(qselects(left + right, k))
	else:
		return left

#O(n^2 + n^2)
def nbestb(a, b):
	best = []
	n = len(a)
	#enumerate
	for x in a:
		for y in b:
			best.append((x,y))
	#qselect
	return qselects(best, n)

#STUDY
 def nbestc(a, b):
	#dijkstras
	
	#use to test if element already used for testing
	def put(i, j):
		#make sure position is valid
		if 0 <= i < n and 0 <= j < n and (i, j) not in used:
			#add to used
			used.add((i, j))
			#push to h the sum, the values, and their position ~ heap organizes based on first element if the value is a list
			heapq.heappush(h, ((sa[i] + sb[j], sb[j]), (sa[i], sb[j]), (i, j)))
			
	#sort a and b
	sa = sorted(a)
	sb = sorted(b)
	n =  len(a)
	h , used = [], set()
	#put the first two values
	put(0, 0)
	
	#loop through n
	for _ in range(n):
		#get the values out of the heap
        _, xy, (i, j) = heapq.heappop(h)
		#yeild
        yield xy
		#put the successors
        put(i+1, j)
        put(i, j+1)

		
	
	
	



a, b = [4, 1, 5, 3], [2, 6, 3, 4]
print(nbesta(a, b))   # algorithm (a), slowest [(1, 2), (1, 3), (3, 2), (1, 4)]
print(nbestb(a, b))   # algorithm (b), slow [(1, 2), (1, 3), (3, 2), (1, 4)]
print(nbestc(a, b))   # algorithm (c), fast [(1, 2), (1, 3), (3, 2), (1, 4)]