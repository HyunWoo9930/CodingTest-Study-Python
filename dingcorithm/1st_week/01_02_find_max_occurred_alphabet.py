def find_max_occurred_alphabet(string):
    alphabet_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'x', 'y', 'z']
    array = find_alphabet_occurrence_array(string)
    max = 0
    max_index = 0
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]
            max_index = i
    return alphabet_array[max_index]


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for i in range(len(string)):
        if string[i] != ' ':
            alphabet_occurrence_array[ord(string[i]) - ord('a')] = alphabet_occurrence_array[
                                                                       ord(string[i]) - ord('a')] + 1
    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
