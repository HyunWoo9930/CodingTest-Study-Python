import math

str = input()
start = int(str.split()[0])
end = int(str.split()[1])


def isDecimal(n):
    max_num = int(math.sqrt(n))
    for i in range(2, max_num + 1):
        if n % i == 0:
            return False
    return True

for i in range(start, end + 1):
    if i == 1:
        continue
    if isDecimal(i) :
        print(i)
