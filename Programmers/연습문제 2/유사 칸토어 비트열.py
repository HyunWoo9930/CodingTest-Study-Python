graph = {
    0 : '1'
}

def solution(n, l, r):
    bit = solution_recursion(n)
    count = 0
    for i in range(l - 1, r, 1):
        if bit[i] == '1':
            count += 1
    return count

def solution_recursion(n):
    index = 1
    while index <= n:
        if n == 0:
            return 1
        else:
            tmp = convert(graph[index - 1])
            graph[index] = tmp
        index += 1
    return graph[n]

def convert(n):
    answer = []
    for i in range(len(n)):
        if n[i] == '1':
            answer.append('11011')
        elif n[i] == '0':
            answer.append('00000')
    return ''.join(answer)

# print(solution(2,4,17))