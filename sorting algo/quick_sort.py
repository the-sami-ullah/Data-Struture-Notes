# we will use quick sort algo. when we want to sort the unstable inplace unique elements in the array. It is a divide and conquer algorithm. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

# worst case time complexity is O(n^2) and best case time complexity is O(n log n). It is not a stable sorting algorithm. It is an in-place sorting algorithm.

def partition(arr, low, high):
    pivot = arr[high]      
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)   
        quick_sort(arr, pi + 1, high)  



arr = [38, 27, 43, 3, 9, 82, 10]

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)