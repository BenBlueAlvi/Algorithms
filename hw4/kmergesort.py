import heapq

#min heap of winners, use replace
#should be nlogn

def _kmergesort(arr, k):
	#partition
	for i in range(k-1):
		_kmergesort(arr[i * len(arr)/k:(i+1) * len(arr)/k], k)
		
	merge(arr)

def merge(arr):
	

def kmergesort(arr, k):
	