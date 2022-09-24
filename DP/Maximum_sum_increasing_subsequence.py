# def maxSumIS(Arr, n):
#     # code here
#     dp = {}
#     def finaMaxSubs(i, prev):
#         if i==n:
#             return 0
#         if (prev,i) in dp:
#             return dp[(prev,i)]
            
#         if prev<Arr[i]:
#             dp[(prev,i)] = max(Arr[i]+finaMaxSubs(i+1, Arr[i]), finaMaxSubs(i+1, prev))
#         else:
#             dp[(prev,i)] = finaMaxSubs(i+1,prev)
#         return dp[(prev,i)]
    
#     return finaMaxSubs(0,-1)


def maxSumIS(Arr, n):
    dp = [Arr[i] for i in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if Arr[i]<Arr[j]:
                dp[j] = max(Arr[j]+dp[i], dp[j])
            # else:
            #     dp[j] = dp[i]
    print(dp)            
    return max(dp)

print(maxSumIS([1, 101, 2, 3, 100],5))




