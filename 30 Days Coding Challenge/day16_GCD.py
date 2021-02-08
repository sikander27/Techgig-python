'''
For this challenge, you need to take input of two numbers , 
calculate their greatest common divisor (GCD) and print it to the stdout

'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT



def gcd(a, b):
    # everything divides zero
    if (b == 0):
        return a
    return gcd(b, a%b)



def main():
    x, y = map(int, input().split())

    print(gcd(x, y))
 

main()

