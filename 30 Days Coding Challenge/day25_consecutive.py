'''
Consecutive!!! (100 Marks)
For this challenge, you need to take number of elements as input on one line and
 array elements as an input on another line. You need to tell whether the 
 numbers present in the array are consecutive or not.

Input Format
In this challenge, you will take number of elements as input on one line and
 array elements which are space separated as input on another line. 


 Explanation
All the elements in the given array have a difference of 1 to the previous element.
 Thus, they are consecutive.
'''





''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if n == 0:
        flag = 0
    else:
        flag = 1
        for i in range(n):
            if i == (n-1):
                continue
            j = i + 1
            if arr[j] - arr[i] == 1:
                continue
            else:
                flag = 0
                break
    
    if flag:
        print(True)
    else:
        print(False)

 # Write code her

main()

