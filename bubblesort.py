def bubblesort(arr):
    no=len(arr)
    for i in range(no):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
                break
arr=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    a=int(input("enter the elements in the list"))
    arr.append(a)
print("The arrray before sorting: ",arr) 
bubblesort(arr)
print('The sorted array is: ',arr)
