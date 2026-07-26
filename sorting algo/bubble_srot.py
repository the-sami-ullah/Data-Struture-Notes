def bubble_sort(arr):
  
  for i in range(len(arr)):
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
  return arr      


arr = [38, 27, 43, 3, 9, 82, 10]
print("Origional array" , arr)
choice  = input(" a)asending  b) desending")
if choice == "a":
    print("Sorted array " , bubble_sort(arr))
else:
    arr = bubble_sort(arr)
    arr.reverse()
    print("Sorted array " , arr )
      

        
        