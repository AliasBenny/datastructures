def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
arr=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    a=int(input("enter the elements in the list"))
    arr.append(a)
print("The arrray before sorting: ",arr) 
insertion(arr)
print('The sorted array os: ',arr)