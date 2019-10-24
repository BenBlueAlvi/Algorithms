import heapq

#k smallest in big array, lazy lists and real lists
#output should be sorted
#k << n
#O(klogk + n(2logk) + k + k + k) =
#(O(nlogk))
def _ksmallest(k, arr):
	s = []# only holds k elements, check if new element is worse or better
	if k > len(arr): k = len(arr)
	#use min heap as max heap with negative numbers
	for i in range(k):
		heapq.heappush(s, -arr[i])
	i = k
	while (i < len(arr)):
		#check for if incoming is worse than greatest arr of k
		if (-arr[i] < s[0]):
			i+=1
			continue
		else:
			#use replace max value with new lesserval
			heapq.heapreplace(s, -arr[i])
		i+=1
	#make the heap a min heap again, so we can pop the numbers in the correct, sorted order
	for i in range(len(s)):
		s[i] = -s[i]
	heapq.heapify(s)
	#yield the numbers
	for i in range(len(s)):
		yield heapq.heappop(s)
		
def ksmallest(k, arr):
	return [i for i in _ksmallest(k, arr)]
	

print(ksmallest(3, range(1000000, 0, -1)))
print(ksmallest(3, [10, 2, 9, 3, 7, 8, 11, 5, 2, 9, 3, 7, 8, 11,9, 3, 7, 8, 7])) #2, 2, 3