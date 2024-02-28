def binarySearch(arr, l, r, x):
     
    while l <= r:
 
        mid = l + (r - l) // 2
 
        
        if arr[mid] == x:
            return mid
 
        
        elif arr[mid] < x:
            l = mid + 1
 
        
        else:
            r = mid - 1
 
    
    return -1
 
 

arr = []
n=int(input("enter the no of elements"))
for i in range(n):
    a=int(input("enter the element"))
    arr.append(a)
x=int(input("enter the no to be searched"))
   
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")