# Minimize the Heights II

def getMinDiff(arr, n, k):
    def greedy(arr,k,count,mini,maxi):
        print(arr)  
        if arr[count-1]>maxi:
            maxi=arr[count-1]
        elif arr[count-1]<mini:
            mini=arr[count-1]
        if count==len(arr):
            print(maxi,mini)
            return maxi-mini
              
        arr[count] +=k
        first = greedy(arr,k,count+1,mini,maxi)
        arr[count] -=(2*k)
        second = 1e9+7
        if arr[0]>=0:
            second = greedy(arr,k,count+1,mini,maxi)
        arr[count] +=k
        return min(first,second)

    mini = 0
    maxi = 0
    arr[0] +=k
    # if arr[0]>maxi:
    #     maxi=arr[0]
    # elif arr[0]<mini:
    #     mini=arr[0]
    first = greedy(arr,k,1,arr[0],arr[0])
    arr[0] -=(2*k)
    second = 1e9+7
    if arr[0]>=0:
        second = greedy(arr,k,1,arr[0],arr[0])
    arr[0] +=k
    return min(first,second)
    
            
arr = list(map(int,input().split()))
n = len(arr)
k = int(input())
print(getMinDiff(arr,n,k))

