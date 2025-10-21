def solution(p):
    if isRight(p):
        return p

    return recursion(p)


def recursion(p):
    u = ''
    v = ''
    for i in range(2, len(p) + 1, 2):
        if isBalance(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if isRight(u):
        if v == '':
            return u
        return u + recursion(v)
    else :
        u = u[1:len(u) - 1]
        if u == '':
            return '(' + recursion(v) + ')'
        else :
            new_u = ''
            for i in u:
                if i == '(':
                    new_u += ')'
                else :
                    new_u += '('

            return '(' + recursion(v) + ')' + new_u

def isRight(s):
    answer = True
    stack = []

    if s.startswith(')') or s.endswith('(') or s.count(")") != s.count("("):
        return False

    for i in s:
        if i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(i)

    if len(stack) != 0:
        answer = False
    return answer


def isBalance(p):
    return p.count('(') == p.count(')')


# print(solution("(()())()"))
# print(solution(")("))
# print(solution("()))((()"))
