
'''
Write a function to take an input and convert binary into decimal form.
'''
def binToDec(n):
    decimal,i = 0, 0
    while n!=0:
        dec = n % 10
        decimal = decimal + dec * pow(2,i)
        n = n // 10
        i += 1
    print(decimal)

def main():
    n = int(input(),2) #using build in function
    # print(n)
    binToDec(n) #using user-defined function
main()