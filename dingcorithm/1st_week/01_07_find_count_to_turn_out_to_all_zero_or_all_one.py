input = input()


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    input_list = []
    input_list.append(string[0])
    for i in range(1, len(string)):
        num = input_list.pop()
        if string[i] == num:
            input_list.append(num)
        else:
            input_list.append(num)
            input_list.append(string[i])

    zero_count = input_list.count('0')
    one_count = input_list.count('1')

    return min(zero_count, one_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
