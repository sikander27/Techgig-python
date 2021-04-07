#practice.py

def mergefunction(left, right):
    result,left_index, right_index = [], 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    mergeArray = result + left[left_index:] + right[right_index:]
    return mergeArray

def mergesort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr)//2
    left = arr[0:middle]
    right = arr[middle:]

    return mergefunction(mergesort(left), mergesort(right))

def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def insertionSort(arr):

    for i in range(1, len(arr)):
        # print("loop {}".format(i))
        key = arr[i] # 2
        j = i - 1 
        while j >=0 and key < arr[j]:
            # print("In while loop {} with key as {} and element as".format(j, key, arr[j]))
            arr[j+1] = arr[j] 
            j -= 1
            # print(arr)
        arr[j+1] = key    
        # print("######", arr)    
    return arr


num = [2, 4, 7 , 100, 124, 97, 83, 27, 154]

sort_num = insertionSort(num)
# bubble= bubbleSort(num)
# print(sort_num)
print(sort_num)


