# Kadane's Algorithm

def maxSubArraySum(arr,N):
    end=0
    add = 0
    maxi = -1e9-7
    while end<N:
        add+=arr[end]
        if add>maxi:
            maxi=add
        if add<=0:
            add=0
        end+=1
    
    return maxi

arr = list(map(int,input().split()))
print(maxSubArraySum(arr,len(arr)))