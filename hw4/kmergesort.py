from heapq import heapify, heappop, heapreplace

#min heap of winners, use replace
#should be nlogn

#STUDY, will be on midterm

def kmergesort(arr, k):
	#partition
	leng = len(arr)
	split = (leng-1) // k + 1
	
	#run all the mergesorts
	lists = [kmergesort(arr[i:i+split], k) for i in range(0, leng, split)]
		
	return merge(lists)
	

def merge(lists):
	heap = [(next(a), i, 0) for i, a in enumerate(map(iter, lists))]
	heapify(heap)
	while heap != []:
		x, i, j = heappop(heap)
		yield x
		try:
			heapreplace(heap, (next(a), i, a))
		except StopIteration:
			heappop(heap)
		

def kmergesort(arr, k):
	