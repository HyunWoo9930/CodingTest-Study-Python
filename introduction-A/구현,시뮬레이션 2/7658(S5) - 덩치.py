def isBigger(a, b):
    if a[1] < b[1]:
        if a[2] < b[2]:
            return 1
        else: return None
    elif a[1] > b[1]:
        if a[2] > b[2]:
            return 0
        else: return None
    return None


n = int(input())

lists = []

for i in range(n):
    weight, height = input().split()
    lists.append([i, int(weight), int(height)])

result = []
for i in range(n):
    count = 1
    for j in range(i):
        if isBigger(lists[i], lists[j]) == 1:
            count+=1
    for j in range(i+1, n):
        if isBigger(lists[i], lists[j]) == 1:
            count+=1
    result.append(count)

print(*result)