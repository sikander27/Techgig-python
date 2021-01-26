num = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 27, 95]


# this is the main method that performs the merging 
def mergeFunc(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
# looping while 
    while leftIndex < len(left) and rightIndex < len(right) :
        # comparing two array element
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    mergeArray = result + left[leftIndex:] + right[rightIndex:]
    # print(mergeArray)
    return mergeArray


# This is a recursive method who main funtion is to split list into half
def mergeSort(array):
    if len(array) == 1:
        return array
    
    middle = len(array)//2
    left = array[0:middle]
    right = array[middle:]
    # print(left, right)
      
    return mergeFunc(mergeSort(left), mergeSort(right) )

 
answer  = mergeSort(num)
print(answer)

