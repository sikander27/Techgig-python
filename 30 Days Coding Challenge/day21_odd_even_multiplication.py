'''
Multiplication between odd and even (100 Marks)
For this challenge, you need to take number of elements as input on one line 
and array elements as an input on another line. You need to find the numbers that are odd, 
add them.
 find the numbers that are even add them and 
 then multiply the two values that you get after addition of even numbers and 
 that of addition of odd numbers.
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    even, odd = 0, 0
    for i in arr:
        if i%2 == 0:
            even += i
        else:
            odd += i
    print(even*odd)

 # Write code here 

# main()

# write a function to check whether a number is odd or even without using % or / operator
def checkEven(a):
    print(bin(a))
    print(bin(1))
    print(a&1)
    if a&1 == 1:

        return 'Odd'
    else:
        return 'even'

print(checkEven(71))
