from collections import deque

# 입력 받기
row = input()
row_x = int(row.split()[0])  # N (세로)
row_y = int(row.split()[1])  # M (가로)

# 미로 입력
maze = []
for i in range(row_x):
    line = input()
    line_arr = []
    for j in line:
        line_arr.append(int(j))
    maze.append(line_arr)

# 거리를 저장할 배열 (0으로 초기화하면 방문 여부도 체크 가능)
distance = [[0 for _ in range(row_y)] for _ in range(row_x)]

queue = deque()
queue.append([0, 0])
distance[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    next = queue.popleft()
    x = next[0]
    y = next[1]
    if x == row_x - 1 and y == row_y - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row_x and 0 <= ny < row_y:
            if maze[nx][ny] == 1 and distance[nx][ny] == 0:
                queue.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1

print(distance[row_x - 1][row_y - 1])
