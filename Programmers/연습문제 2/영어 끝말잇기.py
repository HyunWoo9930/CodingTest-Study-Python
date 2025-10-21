def solution(n, words):
    used = []
    answer_index = 0
    for i in range(len(words)):
        current_word = words[i]
        if i == 0:
            used.append(current_word)
            continue
        if not isCorrect(used, current_word):
            answer_index = i + 1
            break

        used.append(current_word)

    a = answer_index // n
    b = answer_index % n
    if b == 0:
        if a == 0:
            answer = [0, 0]
        else : answer = [n, a]
    else :
        answer = [b, a + 1]
    return answer


def isCorrect(words, value):
    if words.__contains__(value):
        return False
    if not words[-1].endswith(value[0]):
        return False

    return True


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5,
#                ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
#                 "gather", "refer", "reference", "estimate", "executive"]))
# print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
