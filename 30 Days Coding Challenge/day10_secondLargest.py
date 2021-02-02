"""
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line
 and find the second largest array element and print that element to the stdout.

"""

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    length = int(input())
    num = input().split()
    array = list(map(int, num))
    array.sort(reverse = True)

    print(array[1])
 # Write code here 

main()

