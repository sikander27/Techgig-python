'''
You need to input N words one on each line and output should be lexicographically sorted 
i.e the words which comes as a output should be alphabetically sorted
'''

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    limit = int(input())
    words = []
    for i in range(limit):
        words.append(input())
    words.sort()
    for i in words:
        print(i)
    # print(words)

main()

