def linear_search(arr, target):

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9]
    target_value = 5
    result = linear_search(nums, target_value)
    if result != -1:
        print(f"Found {target_value} at index {result}")
    else:
        print(f"{target_value} not found")
