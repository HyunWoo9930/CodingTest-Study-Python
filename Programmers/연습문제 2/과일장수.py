import heapq

def solution(k, m, score):
    answer = 0
    answer_arr = [[] for _ in range(len(score) // m)]

    heap = []

    for i in score:
        heapq.heappush(heap, i * -1)

    for i in range(len(score) // m):
        for j in range(m):
            tmp_arr = answer_arr[i]
            tmp_arr.append(heapq.heappop(heap) * -1)
            answer_arr[i] = tmp_arr

    for i in range(len(score) // m):
        answer += getMin(answer_arr[i]) * m

    return answer

def getMin(array) :
    min = 10
    for i in array:
        if min > i:
            min = i

    return min

# print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
