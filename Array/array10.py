# Minimum number of jumps

def minJumps(arr, n):
    # print(arr)
    jumps = [1e9+7]*n
    jumps[n-1] = 0
    
    for i in range(n-2,-1,-1): 
        # print(i,i+arr[i])
        if i+arr[i]>=n-1:
            jumps[i]=1
        else:
            # print("working",i)
            if arr[i]<=0:
                jumps[i]=-1
                continue
            mini= 1e9+7
            miniIndex = None
            for j in range(i+1,i+arr[i]+1):
                if jumps[j]<mini and jumps[j]>0:
                    # print("check")
                    mini=jumps[j]
                    miniIndex = j

            
            try:
                jumps[i] = 1+jumps[miniIndex]
            except:
                jumps[i] = -1
                # print("check",arr.index(max(arr[i+1:i+arr[i]+1])))
            
        # print(jumps)
    return -1 if jumps[i]==0 else jumps[0] 



# arr = [1, 0, 0, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
# arr = [1, 4, 3, 2, 6, 7]
# arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 2, 0, 8, 9, 2, 6, 7, 6, -1, 9]
print(minJumps(arr,len(arr)))
