
#Radix Sort: Use for large sets of integers with a fixed number of digits.

#logic: Radix sort is a non-comparative sorting algorithm that sorts numbers by processing individual digits. It works by distributing the numbers into buckets based on their digits, starting from the least significant digit to the most significant digit. The algorithm uses a stable sorting algorithm (like counting sort) as a subroutine to sort the numbers based on each digit.

# time complexity: The time complexity of radix sort is O(d * (n + k)), where d is the number of digits in the maximum number, n is the number of elements in the input array, and k is the range of the input (the maximum value). In practice, radix sort can be very efficient for sorting large sets of numbers with a limited range of values.

# Distribute numbers into buckets based on the current digit, collect them back in the same order (FIFO), and repeat for each digit until the array is sorted.




def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1  

    while max_num // exp > 0:
        # Create 10 buckets (0-9)
        buckets = [[] for _ in range(10)]

        # Put numbers into buckets (FIFO)
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        # Collect numbers back
        index = 0
        for bucket in buckets:
            for num in bucket:
                arr[index] = num
                index += 1

        exp *= 10

    


# Example
arr = [2000, 10, 20, 305, 45, 100]
print("Original:", arr)

radix_sort(arr)

print("Sorted:  ", arr)