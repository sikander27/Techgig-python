'''
Minimum effort - Maximum output (100 Marks)
For this challenge, Given an unsorted array arr[0..n-1] of size n, 
find the minimum length subarray arr[s..e] such that sorting this subarray makes the whole array sorted.
'''

''' Read input from STDIN. Print your output to STDOUT 
INPUT=> 13
1 2 4 7 10 11 7 12 3 7 16 18 19
OUTPUT=>4 7 10 11 7 12 3 7
'''

def printUnsorted(arr, n): 
	e = n-1
	# step 1(a) of above algo 
	for s in range(0,n-1): 
		if arr[s] > arr[s+1]: 
			break
		
	if s == n-1: 
		print ("The complete array is sorted") 
		exit() 

	# step 1(b) of above algo 
	e= n-1
	while e > 0: 
		if arr[e] < arr[e-1]: 
			break
		e -= 1

	# step 2(a) of above algo 
	max = arr[s] 
	min = arr[s] 
	for i in range(s+1,e+1): 
		if arr[i] > max: 
			max = arr[i] 
		if arr[i] < min: 
			min = arr[i] 
			
	# step 2(b) of above algo 
	for i in range(s): 
		if arr[i] > min: 
			s = i 
			break

	# step 2(c) of above algo 
	i = n-1
	while i >= e+1:
		if arr[i] < max: 
			e = i 
			break
		i -= 1
	sub_array= list(map(str,arr[s:e+1]))
	print (" ".join(sub_array))


def main():
    arr_size = int(input())
    arr = list(map(int, input().split()))
    
    printUnsorted(arr, arr_size) 
main()

