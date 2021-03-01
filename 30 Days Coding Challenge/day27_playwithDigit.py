'''

Play with digits of a number (100 Marks)
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in that number, identify digits that are odd and add them, identify which digits are even and add them. Subtract the smaller with the larger one.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 
'''


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    digi, even, odd = 0, [], []
    while n >0:
       digi = n % 10
       if digi % 2 == 0:
           even.append(digi)
       else:
           odd.append(digi)
       n = n // 10
    if len(even) == 0:
        sum_e = 0
    else:
        sum_e = sum(even)
    if len(odd) == 0:
        sum_o = 0
    else:
        sum_o = sum(odd)
    if sum_e>sum_o:
        print(sum_e - sum_o)
    else:
        print(sum_o-sum_e)

 # Write code here 

main()

