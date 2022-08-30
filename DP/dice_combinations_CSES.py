n = int(input())
dp = [0]*(n+1)

dp[0]=dp[1]=1
mod = 1e9+7
for i in range(2,n+1):
    for j in range(1,7):
        if j>i:
            break
        dp[i] = (dp[i]%mod+dp[i-j]%mod)%mod
        # dp[i] = (dp[i]+dp[i-j])%mod   # it is similar to that of above statement
        # because (a+b)%mod = (a%mod + b%mod)%mod

print("Answer is => ",dp[n])

