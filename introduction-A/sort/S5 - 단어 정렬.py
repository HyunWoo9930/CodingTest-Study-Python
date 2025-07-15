n = int(input())
lists = list(set(list(input() for _ in range(n))))

lists.sort(key=lambda x: (len(x), x.split()[0]))

for _ in range(len(lists)):
    print(lists[_])