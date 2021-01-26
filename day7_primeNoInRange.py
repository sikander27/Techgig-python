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

