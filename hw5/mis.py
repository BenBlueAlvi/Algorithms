

#list
#linear chain graph: 1 -- 2 -- 4 -- 3 -- 5
#choose numbers form list, but not two consecutive numbers
#max sum of numbers


'''

10 - (10 - 2) = 2
8 - (8 - 5) = 5


F(n)
[n-2] [choose last] 
[n-1] [don't choose last]

Choose bigger between last and biggest of other
F(n) = max(f(n-2) + a[n], f(n-1))
F(n) = 

complexity: 1 + T(n-2) + T(n-1)
1 + (1 + T(n-4) + T(n-3)) + (1 + T(n-3) + T(n-2))
T(n-4) + 2T(n-3) + T(n-2)
T(n-6) + T(n-5) + 2T(n-5) + 2T(n-4) + T(n-4) + T(n-3)
T(n-6) + 3T(n-5) + 3T(n-4) + T(n-3)
T(n-k) + k/2T(n-(k-1)) + k/2T(n-(k-2)) ... T(n - k/2)
n <= k <= n+1

T(0) + n/2T(1) + n/2T(2)... T(n/2)
O(2n + 1)

'''
#

def _max_wis(arr, n, sums):
	#check for if value is unknown
	if (n not in sums):
		#get max between choosing last vs not choosing last
		v1, v2 = _max_wis(arr, n-2, sums), _max_wis(arr, n-1, sums)
		#check for which one was max again
		sums[n] = (v1[0] + arr[n-1], v1[1] + [arr[n-1]]) if max(v1[0] + arr[n-1], v2[0]) == v1[0] + arr[n-1] else (v2[0], v2[1])
	
	return sums[n]
	
def max_wis(arr):
	return _max_wis(arr, len(arr), {-1 : (0, []), 0 : (0, [])})
	


