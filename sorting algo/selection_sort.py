def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
    