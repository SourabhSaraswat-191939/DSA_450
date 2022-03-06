# Cyclically rotate an array by one

def rotate(arr, n):
    for i in range(1,n):
        arr[-i],arr[-i-1]=arr[-i-1],arr[-i]

    return arr

arr = list(map(int,input().split()))
print(rotate(arr,len(arr)))

# Cyclically rotate an array by k times

def rotateK(arr,n,k):
    def reverse(start,end):
        while start<end:
            arr[start],arr[end] = arr[end],arr[start]
            start+=1
            end-=1
    reverse(n-k,n-1)
    reverse(0,n-k-1)
    reverse(0,n-1)
    return arr

array = [1,2,3,4,5,6,7,8,9,0]
k=3
print(rotateK(array,len(array),k))

