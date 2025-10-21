import heapq
import string

def solution(X, Y):
    x_array = [0 for _ in range(10)]
    y_array = [0 for _ in range(10)]

    for i in X:
        x_array[int(i)] = x_array[int(i)] + 1

    for i in Y:
        y_array[int(i)] = y_array[int(i)] + 1

    overlap = [0 for _ in range(10)]
    for i in range(10):
        if x_array[i] <= y_array[i]:
            overlap[i] = x_array[i]
        else:
            overlap[i] = y_array[i]

    if overlap.count(0) == 10:
        return '-1'
    elif overlap.count(0) == 9 and overlap[0] != 0:
        return '0'

    answer_array = []
    for i in range(9,-1,-1):
        for j in range(overlap[i]):
            answer_array.append(str(i))

    answer = ''.join(answer_array)

    return answer

print(solution('100', '2345'))
print(solution('100', '203045'))
print(solution('100', '123450'))
print(solution('12321', '42531'))
print(solution('5525', '1255'))