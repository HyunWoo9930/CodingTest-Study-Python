N = int(input())

# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4

def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return dp(n - 1) + dp(n - 2) + dp(n - 3)


for i in range(N):
    n = int(input())
    print(dp(n))
