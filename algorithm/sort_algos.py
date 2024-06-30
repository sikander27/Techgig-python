def bubbleSort(arr):
    """
    time-complexity = 
    arr = [4, 1, 3, 5] # 4
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):  # -1 because we are lookin at j + 1 in next line
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [5, 2, 1, 6]
print(bubbleSort(arr))
