'''

For this challenge, you need to take a string as an input from the stdin,
 count the number of uppercase and lowercase letters and print them to the stdout.
'''



''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    str = input()
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            pass
    print(upper)
    print(lower)
 # Write code here 

main()

