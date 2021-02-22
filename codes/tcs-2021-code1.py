'''
=> Write a program to take radius as int input from user and write a function to calculate 
area of circle. 
=> Round the area to precision of 2 decimals.
=> condition: 20<r<30
'''


import math #using math module for getting pi value

#A function to find area of circle
def area(r):
    if 20<r<30:
        area = math.pi * r * r
        print(f'{area:.2f}') #rounding area to precision of 2 decimals
    else:
        print("invalid input")
        return 0

# Main function
def main():
    r = int(input()) #taking input radius from user
    area(r)
main()

