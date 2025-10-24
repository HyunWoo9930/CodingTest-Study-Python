from collections import deque

N = int(input())

map = []

for i in range(N):
    line = input()
    line_arr = []
    for j in line:
        line_arr.append(int(j))
    map.append(line_arr)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False for _ in range(N)] for _ in range(N)]


def bfs(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])
    visited[start_x][start_y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and map[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    count += 1

    return count


result = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            house_count = bfs(i, j)
            result.append(house_count)

result.sort()
print(len(result))
for count in result:
    print(count)