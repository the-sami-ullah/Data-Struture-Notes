import time


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


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


def time_func(sort_func, arr):
    a = arr.copy()

    start = time.perf_counter()
    sort_func(a, 0, len(a) - 1)
    end = time.perf_counter()

    return a, end - start


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    sorted_merge, t_merge = time_func(merge_sort, arr)
    sorted_quick, t_quick = time_func(quick_sort, arr)

    print("Original:", arr)
    print("Merge Sort Result:", sorted_merge)
    print(f"Merge Sort Time: {t_merge:.8f} seconds")

    print("Quick Sort Result:", sorted_quick)
    print(f"Quick Sort Time: {t_quick:.8f} seconds")