
#return find(left) if x < root else find(right)
#midterm week 7
#dynamic programming ~ 
'''
Recursion(devide and conquer) + caching(overlapping subproblems)
simplist is fibbonachi

Naive

O(1.618^n) SLOW!
fib(n):
	return 1 if n <= 2 else fib(n-1) + fib(n-2)
	
fib(n) are computed multiple times

bottom up O(n)
fib0(n):
	a, b = 1, 1
	for i in range(3, n+1):
		a, b = a+b, a
	return a
	
records all previous fibs O(n)
fibs = {1:1, 2:1}
fib1(n):
	if n not in fibs: 
		fibs[n] = fib1(n-1) + fib1(n-2)
	return fibs[n]
'''


#number of bitstrings of length n with no two consecutive 0s

#F(n) ~ reduce to F(1) or where n is a known value
#F(n) = F(n-1) [add 1] + F(n-2) [add 0]

#[n-1] + [1] good!
#[n-2] + [1] + [0] good!

n_bno = {0: 1, 1 : 2}
def num_no(n):
	if (n not in n_bno):
		n_bno[n] = num_no(n-1) + num_no(n-2)
	
	return n_bno[n]
	
	
	
#if last is 1 F(n-1) ~ [n-1] + [1]
#i last is 0  F(n-2) + 1 ~ [n-2] + [1] + [0]

n_byes = {-1 : 0, 0 : 0, 1 : 0, 2 : 1}
#number of bitstrings of n with two consecutive 0s	
def num_yes(n):

	if (n not in n_byes):
		n_byes[n] = num_yes(n-1) + num_yes(n-2) + 2
			
	return n_byes[n]
	
	
print(num_no(3)) #5
print(num_yes(3)) #3
		