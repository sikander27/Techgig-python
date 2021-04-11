
'''
Find max sum of 2 nums whose digits adds up to equal sum
'''

def sumofdigits(num):
    sum = 0
    while num>0:
        d = num % 10
        sum = sum + d
        num = num // 10
    return sum

def solution(A):
    max_sum = -1
    if len(A) <= 0:
        return max_sum
    reference = {}
    for i in A:
        sum = sumofdigits(i) # 6
        if sum in reference:
            cmax = i + reference[sum]
            if cmax > max_sum:
                max_sum = cmax
        else:
            reference[sum] = i
    return max_sum


def solutions(A):
    if len(A) <= 0:
        return 0
    reference = {}
    result = []
    for i in A:
        if i in reference:
            n = reference[i] + 1
            reference[i] = n
        else:
            reference[i] = 1
    for i,j in reference.items():
        if i == j:
            result.append(i)
    if len(result) == 0:
        return 0
    return max(result)

a = solution([3,3,2,2,5,5,5,5,5,4,3])
a = solution([])
print(a)




'''
calculate the minimum number of letters that must be removed to make it palindrome
'''