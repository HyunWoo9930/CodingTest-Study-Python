n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, target, depth):
    visited[node] = True

    if node == target:
        return depth

    for next_node in graph[node]:
        if not visited[next_node]:
            result = dfs(next_node, target, depth + 1)
            if result != -1:  # 경로를 찾았다면
                return result

    return -1  # 경로를 찾지 못했다면


answer = dfs(start, end, 0)
print(answer)