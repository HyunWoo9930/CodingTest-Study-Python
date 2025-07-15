n = int(input())

lists = []

lists.append(0)
lists.append(1)

for i in range(2, n+1):
    lists.append(lists[i-2] + lists[i-1])

print(lists[n])