'''


[1, 2, 3, 4, 5, 6]


'''


#O(n^2)
def find(arr):
	#sort it
	
	
	
	triples = []
	
	#find pairs in arr that add up to z
	
	#naive
	#do in nlogn, sort!
	arr.sort()
	#use two pointers
	'''for i, x in enumerate(arr[:-1]):
		for i, y in enumerate(arr[i+1:]):
			if (x + y == z)'''
	print(arr)
	#O(n)	
	for z in arr:
		#O(n)
		x = 0
		y = len(arr)-1
		#two pointers
		while(x < len(arr) and y > 0):
		
			
			#if sum is greater than z, move y to decrease value
			if (arr[x] + arr[y] > z):
				y -= 1
				
			#if sum is less than z, move x to increase value
			elif (arr[x] + arr[y] < z):
				x += 1
				
			#if equal
			elif (arr[x] + arr[y] == z):
				#make sure y value is greater than x value so no dups
				if (arr[y] > arr[x]): triples.append((arr[x], arr[y], z))
				#move both pointers
				y -= 1
				x += 1
			
				
	return triples
			

	
					
