def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr    

arr = [38, 27, 43, 3, 9, 82, 10]
result = []
for i in range(len(arr)):
    if i % 2 == 0:
      result.append(arr[i])
print(result)      

print("Origional array" ,arr )

choice  = input(" a)asending  b) desending")

result = insertion_sort(result)
print(result)



for i in range(len(arr)):
    if i % 2 == 0:
        
        arr[i] = result[i // 2]
    
      
      
      

if choice == "a":
    print("Sorted array " , arr)
else:
    arr.reverse()
    print("Sorted array " , arr )


      