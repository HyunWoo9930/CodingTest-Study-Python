def summarize_string(input_str):
    stack_list = [[input_str[0], 1]]
    for i in range(1, len(input_str)):
        index = stack_list.pop()
        if index[0] == input_str[i]:
            index[1] += 1
            stack_list.append(index)
        else:
            stack_list.append(index)
            stack_list.append([input_str[i], 1])
    result = ''
    for i in stack_list:
        result += i[0]
        result += str(i[1])
    return result


input_str = "acccdeee"

print(summarize_string(input_str))
