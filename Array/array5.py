# Move all the negative elements to one side of the array 
def twoPointer(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        while arr[start]<0 and start<end:
            start+=1
        while arr[end]>=0 and start<end:
            end-=1
        arr[start],arr[end] = arr[end],arr[start]
    return arr

def quickSort(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]<0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1

    return arr


arr = list(map(int,input().split()))

# print(quickSort(arr))
print(twoPointer(arr))


        