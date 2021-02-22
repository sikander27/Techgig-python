# A Python 3 program to find a maximum 
# product of a quadruple in array of integers 

# Function to find a maximum product of a 
# quadruple in array of integers of size n 
def maxProduct(arr, n): 

	# if size is less than 4, no 
	# quadruple exists 
	if (n < 4): 
		return -1

	# Sort the array in ascending order 
	arr.sort() 

	x = (arr[n - 1] * arr[n - 2] *
		arr[n - 3] * arr[n - 4]) 
	y = arr[0] * arr[1] * arr[2] * arr[3] 
	z = (arr[0] * arr[1] *
		arr[n - 1] * arr[n - 2]) 

	# Return the maximum of x, y and z
	# print(x, y, z)
	return max(x, max(y, z)) 

# Driver Code 
if __name__ == "__main__": 
	
	arr = [ -10, -3, 5, 6, -20 ] 
	n = len(arr) 
	max = maxProduct(arr, n) 
	if (max == -1): 
		print("No Quadruple Exists") 
	else: 
		print("Maximum product is", max) 

# This code is contributed by ita_c 
