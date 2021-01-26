"""
For this challenge, you need to read a integer value(default name - age) from stdin, store it in a variable and then compare that value with the conditions given below -
    - if age is less than 10, then print 'I am happy as having no responsibilities.' to the stdout.
    - if age is equal to or greater than 10 but less than 18, then print 'I am still happy but starts feeling pressure of life.' to the stdout.
    - if age is equal to or greater than 18, then print 'I am very much happy as i handled the pressure very well.' to the stdout. 

"""
def main():
    age  = int(input())
    if age < 10:
        print("I am happy as having no responsibilities.")
    elif age >= 10 and age < 18:
        print("I am still happy but starts feeling pressure of life.")
    elif age >=18:
        print("I am very much happy as i handled the pressure very well.")
    else:
        print("Invalid Input")

main()