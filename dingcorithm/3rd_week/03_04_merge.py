array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array1_index = 0
    array2_index = 0
    result_array = []

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] <= array2[array2_index]:
            result_array.append(array1[array1_index])
            array1_index += 1
        else:
            result_array.append(array2[array2_index])
            array2_index += 1

    # extend로 남은 요소 한번에 추가
    result_array.extend(array1[array1_index:])
    result_array.extend(array2[array2_index:])

    return result_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))