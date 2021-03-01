''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    max_n = max(arr)
    min_n = min(arr)
 
    print(max_n * min_n)

main()

