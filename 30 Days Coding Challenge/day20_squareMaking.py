'''
Square making (100 Marks)
You need to print the following pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    i,j = 5, 5
    for i in range(5):
        for j in range(5):
            if j == 4:
                print('*', end="")
            else:
                print('*', end=" ")
        print("")

 # Write code here 

main()

