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


