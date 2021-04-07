'''
Compare two numbers (100 Marks)
For this challenge, you will take two integers input from stdin, 


Input=> 345678   444444
Outpu=> 345678
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def sum_digit(n):
    digi, total = 0, 0
    while n >0:
        digi = n % 10
        total = total + digi
        n = n // 10
    return total

def main():
    n, m = map(int,input().split())
    sum_n = sum_digit(n)
    sum_m = sum_digit(m)
    if sum_n > sum_m:
        print(n)
    elif sum_n == sum_m:
        print('Equal')
    else:
        print(m)
   
 # Write code here 

main()

