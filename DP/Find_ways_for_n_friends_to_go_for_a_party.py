n = int(input())
dp = [-1]*(n+1)

def find(n):
    if n==1 or n==0:
        return 1
    if dp[n]!=-1:
        return dp[n]

    dp[n] = find(n-1) + (n-1)*find(n-2)
    return dp[n]

print("Answer is => ",find(n))