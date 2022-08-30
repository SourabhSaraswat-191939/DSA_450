n = int(input())
arr = list(map(int,input().split()))
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = abs(arr[1]-arr[0])

# top-down approach
def find(n):
    if dp[n]!=-1:
        return dp[n]
    dp[n] = min(find(n-1)+abs(arr[n]-arr[n-1]), find(n-2)+abs(arr[n]-arr[n-2]))
    return dp[n]

print("Answer is => ",find(n-1))

# bottom-up approach
dp2 = [-1]*(n+1)
dp2[0] = 0
dp2[1] = abs(arr[1]-arr[0])
for i in range(2,n):
    dp2[i] = min(dp2[i-1]+abs(arr[i]-arr[i-1]),dp2[i-2]+abs(arr[i]-arr[i-2]))

print("Answer is => ",dp2[n-1])

# bottom-up approach with T.C.-> O(n) and S.C.-> O(1)
first = 0
second = abs(arr[1]-arr[0])
for i in range(2,n):
    ans = min(second+abs(arr[i]-arr[i-1]),first+abs(arr[i]-arr[i-2]))
    first = second
    second = ans

print("Answer is => ",ans)