def solution(s):
    answer = True
    stack = []

    if s.startswith(')') or s.endswith('(') or s.count(")") != s.count("("):
        return False

    for i in s:
        if i == ')':
            if isEmpty(stack):
                return False
            else:
                stack.pop()
        else:
            stack.append(i)

    if not isEmpty(stack):
        answer = False
    return answer


def isEmpty(stack):
    return stack.count('(') == 0


print(solution('()()'))
print(solution('(()()())'))
print(solution(')()('))
print(solution('(()('))
