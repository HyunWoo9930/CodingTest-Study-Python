import math

M, N = input().split()
M = int(M)
N = int(N)


def isDecimal(n):
    prime_list = []
    for i in range(2, n + 1):
        for j in prime_list:
            if j * j <= i and i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


for i in isDecimal(N):
    if M <= i <= N:
        print(i)
