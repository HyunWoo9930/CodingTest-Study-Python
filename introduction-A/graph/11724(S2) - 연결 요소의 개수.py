import sys

sys.setrecursionlimit(10 ** 6)

# 1. 문제의 input을 받습니다.
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 2. 탐색을 위한 배열을 초기화 합니다.
visited = [False for _ in range(N + 1)]


# 3. 연결요소 탐색을 위한 dfs를 구현합니다.
def dfs(node):
    visited[node] = True
    for x in graph[node]:
        if not visited[x]:
            dfs(x)


# 4. 그래프 정점들을 탐색하며 연결요소의 개수를 구합니다.
ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        ans += 1
        dfs(i)
print(ans)
