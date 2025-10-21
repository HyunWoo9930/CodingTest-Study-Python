def solution(s):
    min = len(s)
    for i in range(len(s) // 2):
        n = split_represent(s, i + 1)
        if min > n:
            min = n
    answer = min
    return answer


def split_represent(s, n):
    stack = []
    split_string = split(s, n)
    for i in split_string:
        if i == '':
            continue
        if len(stack) == 0:
            stack.append([1, i])
        else:
            prev = stack.pop()
            if prev[1] == i:
                prev[0] = prev[0] + 1
                stack.append(prev)
            else :
                stack.append(prev)
                stack.append([1, i])

    count = 0
    for i in stack:
        if i[0] != 1:
            count += len(str(i[0]))
        count += len(i[1])

    return count

def split(s, n):
    split_string = []
    prev = 0
    for i in range(n, len(s) + 1, n):
        split_string.append(s[prev:i])
        prev = i

    split_string.append(s[prev:])
    return split_string