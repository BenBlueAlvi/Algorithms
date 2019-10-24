

#list
#linear chain graph: 1 -- 2 -- 4 -- 3 -- 5
#choose numbers form list, but not two consecutive numbers
#max sum of numbers


'''

F(n)
[n-2] [choose last] 
[n-1] [don't choose last]

Choose bigger between last and biggest of other
F(n) = max(f(n-2) + a[n], f(n-1))
F(n) = 



'''
#complexity: O(nlogn)?
def _max_wis(arr, n, sums):
	#check for if value is unknown
	if (n not in sums):
		#get max between choosing last vs not choosing last
		v1, v2 = _max_wis(arr, n-2, sums), _max_wis(arr, n-1, sums)
		maxv = max(v1[0] + arr[n-1], v2[0])
		
		#check for which one was max again
		if (maxv == v1[0] + arr[n-1]):
			
			#set sums to the new largest value, and update the two numbers that go into it if there's already two numbers there
			if (len(v1[1]) == 2):
				#save the max previous value
				mv = max(v1[1][0], v1[1][1])
				#figure out whether to replace the last value
				mv2 = max(v1[1][0], arr[n-1]) if mv == v1[1][1] else max(v1[1][1], arr[n-1])
			
				#update sums new max + mv
				sums[n] = (mv + mv2, [mv2, mv])
			else:
				sums[n] = (v1[0] + arr[n-1], v1[1] + [arr[n-1]])
		else:
			sums[n] = (v2[0], v2[1])
		
	return sums[n]
	
def max_wis(arr):
	return _max_wis(arr, len(arr), {-1 : (0, []), 0 : (0, [])})
	
#broken when a lot of elements
print(max_wis([50,8,5,200, 12, 12,100, 4, 12, 0,12])) # (12, [7,5]))
print(max_wis([7,8,5])) #(12, [7,5])
print(max_wis([-1,8,10])) #(10, [10])
print(max_wis([])) #(0, [])
print(max_wis([-5, -1, -4])) #(0, [])

