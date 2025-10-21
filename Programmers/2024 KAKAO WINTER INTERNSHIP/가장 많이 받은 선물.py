def solution(friends, gifts):
    n = len(friends)
    array = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in gifts:
            give = j.split(' ')[0]
            get = j.split(' ')[1]
            if give == friends[i]:
                array[i][getIndex(friends, get)] = array[i][getIndex(friends, get)] + 1

    array_factor = [0 for _ in range(n)]

    for i in range(n):
        give_count = 0
        get_count = 0
        for j in range(n):
            give_count += array[i][j]
            get_count += array[j][i]
        array_factor[i] = give_count - get_count

    array_answer = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                break
            else:
                if array[i][j] > array[j][i]:
                    array_answer[i] = array_answer[i] + 1
                elif array[i][j] < array[j][i]:
                    array_answer[j] = array_answer[j] + 1
                elif array[i][j] == array[j][i]:
                    if array_factor[i] > array_factor[j]:
                        array_answer[i] = array_answer[i] + 1
                    if array_factor[i] < array_factor[j]:
                        array_answer[j] = array_answer[j] + 1
                elif array[i][j] == 0 and array[j][i] == 0:
                    if array_factor[i] > array_factor[j]:
                        array_answer[i] = array_answer[i] + 1
                    if array_factor[i] < array_factor[j]:
                        array_answer[j] = array_answer[j] + 1

    answer = getMax(array_answer)
    return answer


def getIndex(friends, target):
    index = 0
    for i in friends:
        if target == i:
            break
        else:
            index += 1
    return index

def getMax(array):
    max = 0
    for i in array:
        if max <= i:
            max = i
    return max
print(solution(["muzi", "ryan", "frodo", "neo"],
         ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
