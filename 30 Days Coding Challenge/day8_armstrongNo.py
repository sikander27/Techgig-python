"""
For this challenge, you need to take an integer input and store it in a variable of your choice and checks
 whether this number is an Armstrong number or not. If yes print 'True' else print 'False'.
"""


def main():
    a = input()
    length = len(a)
    # print(length)
    temp = int(a)
    num = temp
    sum = 0
    while num>0:
        d = num % 10
        sum = sum + (d**length)
        num = num // 10

    print(sum)
    if sum == temp:
        print("Armstrong Number")
    else:
        print("not armstrong")

main()