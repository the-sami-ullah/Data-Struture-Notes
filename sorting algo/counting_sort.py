


# counting sort Use for large sets of non negative numbers with a limited range of values.

#time complexity: The time complexity of counting sort is O(n + k), where n is the number of elements in the input array and k is the range of the input (the maximum value). 


def countingSort(arr):
    if not arr:
        return arr
        
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)

    

Arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print("unSorted array:", Arr)
countingSort(Arr)
print("Sorted array:", Arr)