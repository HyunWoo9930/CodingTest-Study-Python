numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    get_all_ways_by_doing_plus_or_minus(array, 0, 0)

    count = 0
    for i in result:
        if i == target:
            count += 1
    return count


def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
    if current_index == len(array):
        result.append(current_sum)
        return
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
    get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])


# print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
