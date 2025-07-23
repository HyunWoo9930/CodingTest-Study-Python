while 1:
    n = int(input())
    if n == 0:
        break
    lists = [] * n
    for i in range(n):
        str1 = input()
        lists.append([str1, str1.lower()])
    lists.sort(key=lambda x: x[1])
    print(lists[0][0])