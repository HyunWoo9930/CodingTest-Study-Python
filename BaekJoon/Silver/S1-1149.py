N = int(input())
house = []

for i in range(N):
    house.append(list(map(int, input().split())))

# dp[i][j] = i번째 집을 j색으로 칠했을 때의 최소 비용
dp = [[0] * 3 for _ in range(N)]

# 첫 번째 집 초기화
dp[0] = house[0][:]

# Bottom-up DP
for i in range(1, N):
    dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = house[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = house[i][2] + min(dp[i-1][0], dp[i-1][1])

print(dp)
print(min(dp[N-1]))