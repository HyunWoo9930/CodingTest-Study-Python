n = int(input())
list = []

for i in range(n):
    x, y = input().split()
    list.append([int(x), int(y)])

list.sort(key=lambda x: (x[0], x[1]))

for i in range(len(list)):
    print(list[i][0], list[i][1])
