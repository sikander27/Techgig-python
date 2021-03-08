'''
Comparison between diagonals (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin , 
calculate the sum of the digits for each diagonal and compare them.For example,
in the below matrix
1 2 3
4 5 6
7 8 9
Diagonal 1 is 1,5,9.
Diagonal 2 is 3,5,7.

'''
def main():
    r, c = map(int, input().split())
    mat = []
    for i in range(r):
        row = list(map(int, input().split()))
        mat.append(row)
    sum1,sum2,f,b= 0,0,0,c-1
    for i in range(r):
        sum1 += mat[i][f]
        f += 1
        sum2 += mat[i][b]
        b -= 1
    
    if sum1>sum2:
        print('Diagonal 1')
    elif sum1<sum2:
        print('Diagonal 2')
    else:
        print('Equal')
        
 # Write code here 

main()

