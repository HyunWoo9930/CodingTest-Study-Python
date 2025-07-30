def find_not_repeating_first_character(string):
    distinct = []
    for i in range(len(string)):
        if distinct.__contains__(string[i]):
            continue
        distinct.append(string[i])
        isDuplicate = False
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                isDuplicate = True
                break
        if not isDuplicate:
            return string[i]
    return '_'


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
