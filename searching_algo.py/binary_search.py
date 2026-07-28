def binary_search_iterative(arr, target):
    
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        #shrink the search space
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left=0, right=None):

    #base case
    if right is None:
        right = len(arr) - 1
    #base case
    if left > right:
        return -1

    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    #shrink the search space
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    value = 7

    print("Iterative search:", binary_search_iterative(numbers, value))
    print("Recursive search:", binary_search_recursive(numbers, value))
