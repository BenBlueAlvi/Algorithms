from heapq import heapify, heappop, heapreplace, heappush

#min heap of winners, use replace
#should be nlogn

#STUDY, will be on midterm

def kmergesort(arr, k):
	length = len(m)
	if length <= 1:
		return m
	split = (length-1)//k + 1
	k_lists = [kmergesort(m[i:i+split],k) for i in range(0, length, split)] # no empty sublists
	return list(merge(*k_lists))

def merge(lists):
	#heap sort the lists

	heap = [(a[0], i, 0) for i, a in enumerate(lists)]
	heapify(heap)
	while heap != []:
		x, i, j = heappop(heap)
		yield x
		a = lists[i]
		if j < len(a) - 1:
			heappush(heap, (a[j+1], i, j+1))
		
print(*[1, 2, 3])
print([x for x in merge([[2, 234, 54], [12, 21, 3], [23, 5, 76], [3, 5, 6]])])
	