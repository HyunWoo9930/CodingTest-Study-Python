input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = 1
    while n < len(array):
        target_index = n
        index = n - 1
        while index >= 0:
            if array[index] <= array[target_index]:
                break
            else:
                array[index], array[target_index] = array[target_index], array[index]
                target_index = index
            index -= 1

        n += 1
    return array


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ", insertion_sort([5, 8, 4, 7, 7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", insertion_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", insertion_sort([100, 56, -3, 32, 44]))
