n = int(input())

# dp(x) = min(dp(x/3)+1, dp(x/2)+1, dp(x-1)+1)
dp = [0] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    if i % 3 == 0:
        if i % 2 == 0:
            num = min(dp[int(i // 3)] + 1, dp[int(i // 2)] + 1, dp[i - 1] + 1)
            dp[i] = num
        else:
            num = min(dp[int(i // 3)] + 1, dp[i - 1] + 1)
            dp[i] = num
    elif i % 2 == 0:
        num = min(dp[int(i // 2)] + 1, dp[i - 1] + 1)
        dp[i] = num
    else:
        num = dp[i - 1] + 1
        dp[i] = num

print(dp[n])
