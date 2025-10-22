from collections import deque

line = input()
N = int(line.split()[0])
M = int(line.split()[1])

distance = [0 for _ in range(100000)]

queue = deque()
queue.append(N)
distance[N] = 0

count = 0
while queue:
    x = queue.popleft()

    dx = [-1, 1, x]

    if x == M:
        break

    if x > M:
        nx = x - 1
        if nx > 0 and distance[nx] == 0:
            queue.append(nx)
            distance[nx] = distance[x] + 1
    else:
        for i in range(3):
            nx = x + dx[i]
            if 0 < nx < 100000 and distance[nx] == 0:
                queue.append(nx)
                distance[nx] = distance[x] + 1


print(distance[M])
