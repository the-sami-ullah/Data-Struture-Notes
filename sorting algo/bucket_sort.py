
# Use Bucket Sort when the input data is uniformly distributed over a known range.
# Example: Sorting students' percentages (0–100) or decimal numbers between 0 and 1.

#time complexity: The time complexity of bucket sort is O(n + k), where n is the number of elements in the input array and k is the number of buckets. In practice, bucket sort can be very efficient for sorting large sets of numbers that are uniformly distributed over a known range.



def bucket_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    bucket_count = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Put elements into buckets
    for num in arr:
        index = (num * bucket_count) // (max_val + 1)
        buckets[index].append(num)

    # Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Merge buckets back into the original array
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

    return arr


myArray = [29, 25, 3, 49, 9, 37, 21, 43]

print("Original:", myArray)
bucket_sort(myArray)
print("Sorted:  ", myArray)