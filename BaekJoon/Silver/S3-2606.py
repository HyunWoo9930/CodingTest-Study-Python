count = int(input())
N = int(input())
graph = {}

for i in range(count):
    graph[i + 1] = []

for i in range(N):
    pair = input()
    start_node = int(pair.split()[0])
    end_node = int(pair.split()[1])
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

answer_arr = [False for _ in range(count)]

visited = []
visit = []

# {1: [2, 5], 2: [3], 3: [], 4: [7], 5: [2, 6], 6: [], 7: []}

visit.append(1)
while len(visit) != 0:
    n = visit.pop()
    visited.append(n)
    answer_arr[n - 1] = True
    for i in graph[n]:
        if not visited.__contains__(i):
            visit.append(i)

count = 0

for i in range(len(answer_arr)):
    if i == 0:
        continue
    if answer_arr[i] == True:
        count += 1

print(count)
