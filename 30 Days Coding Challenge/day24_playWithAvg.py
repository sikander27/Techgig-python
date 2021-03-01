''' Read input from STDIN. Print your output to STDOUT 
Play With Average (100 Marks)
For this challenge, you need to take number of elements as input on one line and array elements as an input on another line. You need to find the average of even numbers, then the average of odd numbers and add them (round the averages to the nearest integers).

'''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import math
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    even, odd = [],[]
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else: 
            odd.append(i)
    if (len(even) == 0):
        len_e =  0 
    else:
        len_e = math.ceil(sum(even)/len(even))

    if (len(odd) == 0):
        len_o=  0 
    else:
        len_o = math.ceil(sum(odd)/len(odd))

    result = len_e + len_o

    # result = math.ceil(sum(even)/len(even)) + math.ceil(sum(odd)/len(odd))
    print(result)


 # Write code here 

main()

