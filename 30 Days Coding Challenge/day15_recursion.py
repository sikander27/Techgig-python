'''
This program takes two integers from user ( base number and a exponent) 
 calculates the power. Instead of using loops to calculate power,
  this program uses recursion to calculate the power of a number.

'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def xpower(base, exp):
    if exp == 0:
        return 1 #remember to use 1 as the last value, it's very important
    else:
        return (base * xpower(base, exp-1))

def main():
    x, y = map(int, input().split())
    
    print(xpower(x,y))
    

    
 # Write code here 

main()


