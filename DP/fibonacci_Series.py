n= int(input())

dp = [-1]*(n+1)

def fib(n):
    if n==0 or n==1:
        return 1
    if dp[n]!=-1:
        return dp[n]

    dp[n] = fib(n-1)+fib(n-2)
    return dp[n]

print("Ansewer is => ",fib(n))