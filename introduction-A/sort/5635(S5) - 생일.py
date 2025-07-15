n = int(input())

lists = []

for _ in range(n):
    name, day, month, year = input().split(' ')
    lists.append([name, int(day), int(month), int(year)])

lists.sort(key=lambda x: (x[3], x[2], x[1]))

print(lists[n-1][0])
print(lists[0][0])