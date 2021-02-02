"""
For this challenge, you need to take an integer value as input from stdin, calculate its factorial and print the result to the stdout. 1

"""
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    number = int(input())
    fact = 1
    while number>0:
        fact = number * fact
        number -= 1
    
    print(fact)


main()

