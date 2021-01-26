"""
How Much Big Is Your Number (100 Marks)
For this challenge, you will take an integer input from stdin, 
store it in a variable and  calculate the number of digits in
 the number using division operator
 """
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    num = int(input())
    digit = 0
    while num>0:
        mod = num % 10
        digit +=1
        num = num // 10

    print(digit)
 # Write code here 

main()

