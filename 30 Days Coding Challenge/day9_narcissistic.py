"""
For this challenge, you will take an integer input and 
store it in a variable and checks whether the input number is a Narcissistic number or not.
 If it is, then print 'True' else print 'False'.
 #########################################################
Explanation
First of all, what is a Narcissistic Number?
An n-digit number that is the sum of the nth powers of its digits is called an n-narcissistic number.

For example, take the number 1634

1634 = 1^4 + 6^4 + 3^4 + 4^4
So, this is a Narcissistic Number.


############################################################# 
  """
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    a = input()
    length = len(a)
    num = int(a)
    temp = num 
    sum =0 
    while temp>0:
        t = temp % 10
        sum = sum + ( t ** length)
        temp = temp // 10
    if sum == num:
        print(True)
    else:
        print(False)

 # Write code here 

main()


  