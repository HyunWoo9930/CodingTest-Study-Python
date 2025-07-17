T = int(input())


def test(k, n):
    result = []
    result.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    for i in range(1, k + 1):  # i번째 층
        lists = []
        for j in range(14):  # j번째 호수
            if i == k:
                if j == n:
                    result.append(lists)
                    return result
            sum = 0
            for s in range(j + 1):
                sum += result[i - 1][s]
            lists.append(sum)
        result.append(lists)
    return result


for i in range(T):
    k = int(input())
    n = int(input())
    print(test(k, n)[k][n-1])
