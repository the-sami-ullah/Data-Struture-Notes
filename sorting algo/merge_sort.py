# merge sort is used when we want to sort the stable not inplace unique elements in the array. It is a divide and conquer algorithm. It works by dividing the unsorted list into n sublists, each containing one element (a list of one element is considered sorted), then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

# worst case time complexity is O(n log n) and best case time complexity is O(n log n). It is a stable sorting algorithm. It is not an in-place sorting algorithm.



def merge_sort(arr, low, high):
     
    if low < high:
        mid = (low + high) // 2
        
        merge_sort(arr, low, mid)
        
        merge_sort(arr, mid + 1, high)
        
        merge(arr, low, mid, high)




def merge(arr, low, mid, high):
  
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    
    
    i, j, k = 0, 0, low
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    arr[k:high + 1] = left[i:] + right[j:]


arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)    
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


