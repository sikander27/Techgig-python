"""
 For this challenge, you are given a range and you need to find how many prime numbers
  lying between the given range.
"""
count = 0
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    a = int(input())
    b = int(input())
    count = 0
    for num in range(a, b + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:
                count += 1  
                #    print(num)
      
    print(count)

 # Write code here 

main()

# efficient code
# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 

def SieveOfEratosthenes(n): 
	
	# Create a boolean array "prime[0..n]" and initialize 
	# all entries it as true. A value in prime[i] will 
	# finally be false if i is Not a prime, else true. 
	prime = [True for i in range(n + 1)] 
	p = 2
	while (p * p <= n): 
		
		# If prime[p] is not changed, then it is a prime 
		if (prime[p] == True): 
			
			# Update all multiples of p 
			for i in range(p * 2, n + 1, p): 
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers 
	for p in range(n + 1): 
		if prime[p]: 
			print p, #Use print(p) for python 3 

# driver program 
if __name__=='__main__': 
	n = 30
	print "Following are the prime numbers smaller", 
	#Use print("Following are the prime numbers smaller") for Python 3 
	print "than or equal to", n 
	#Use print("than or equal to", n) for Python 3 
	SieveOfEratosthenes(n) 
