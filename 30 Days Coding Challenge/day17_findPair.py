'''
For this challenge, you need to take array and an integer as an input, 
check for pair in array with sum as that of an integer 
and if you find those two numbers in the array return true else return false.
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
# time complexity of log(N^2)
def main():
    size = int(input())
    arr = list(map(int, input().split()))
    total = int(input())
    flag = False
    arr.sort()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] + arr[j] == total:
                flag = True
                break
    print(flag)   

# main()

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and 
    # use print to write your output to STDOUT

# time complexity of log(N)
def sk_solution():
    size = int(input())
    arr = list(map(int, input().split()))
    total = int(input())
    # arr2 = set()
    arr2 = []
    # flag = False
    # arr.sort()
    for i in arr:
        if i > total:
            continue
        else:
            rem = total - i
            if rem in arr2:
                flag = True
                pair = list(( arr.index(rem), arr.index(i)))
                return pair
                break
            else:
                arr2.append(i)
    # print(arr2)
    # print(flag)   

print(sk_solution())

