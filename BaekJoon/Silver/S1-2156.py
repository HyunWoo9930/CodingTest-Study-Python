N = int(input())

wine = []

for i in range(N):
    wine.append(int(input()))

dp = [0 for _ in range(N)]

if N == 1:
    print(wine[0])
elif N == 2:
    print(wine[0] + wine[1])
elif N == 3:
    print(max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2]))
else:
    dp[0] = wine[0]
    dp[1] = dp[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[0] + wine[2])

    for i in range(3, N):
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])

    print(dp[N - 1])
