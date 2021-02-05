'''
For this challenge, you need to take a matrix as an input from the stdin , 
transpose it and print the resultant matrix to the stdout.
'''
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    ax, ay = map(int, input().split())
    mat = []
    for i in range(ax):
        row = list(map(int, input().split()))
        mat.append(row)
    trans = []
    # changing rows(ax) with column(ay)
    for i in range(ay):
        row = []
        for j in range(ax):
            k = mat[j][i]
            row.append(k)
            if j == ax-1:
                print(k)
            else:
                print(k, end=" ")
        trans.append(row)
    # to print transpose array
    #print(trans)
    

 # Write code here 

main()


