''' Read input from STDIN. Print your output to STDOUT
Biggest Digit In A Number (100 Marks)
For this challenge, you will take an integer input from stdin, store it in a variable, find the digits in a number and then print the biggest of them.

Input Format
A single integer value to be taken as input from stdin and stored it in a variable of your choice. 

 '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    digi,arr= 0, []
    while n>0:
        digi = n % 10
        arr.append(digi)
        n = n//10
    print(max(arr))
 # Write code here 

main()

