'''
Which row is bigger? (100 Marks)
For this challenge, you need to take a matrix as an input from the stdin,
 identify which row has the maximum sum of the digits.For example, in the below matrix
1 2 3
4 5 6
7 8 9
Row 1 is 1,2,3
Row 2 is 4,5,6
Row 3 is 7,8,9

Input Format
The first line contains two integers N, M denoting the number of rows and columns respectively.
Each of the 'N' Next line contains M integers each.
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    r, c = map(int, input().split())
    mat = []
    rows = []
    for i in range(r):
        mat.append(list(map(int,input().split())))
    for i in range(r):
        rows.append(sum(mat[i]))
    
    row_no = rows.index(max(rows))
    print("Row",row_no+1)
    # print(rows)
    
main()

