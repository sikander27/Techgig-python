arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def mergeSort(array):
    if len(array) == 1:
        return array
    
    middle = len(array)//2
    left = array[0:middle]
    right = array[middle:]
    # print(left, right)

    return mergeSort(right)


answer  = mergeSort(arr)
print(answer)

