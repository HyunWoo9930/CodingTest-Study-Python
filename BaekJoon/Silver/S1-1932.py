N = int(input())

triangle = []

for i in range(N):
    line = input()
    arr = []
    for j in line.split():
        arr.append(int(j))
    triangle.append(arr)

dp = []

for i in range(1, N + 1):
    arr = [0 for _ in range(i)]
    dp.append(arr)

dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j])

# for i in dp:
#     print(i)

print(max(dp[N - 1]))
