input = "abcba"


def is_palindrome(string):
    if len(string) == 0:
        return True
    a = string[0]
    b = string[len(string) - 1]
    if a == b:
        is_palindrome(string[1:len(string) - 1])

    return True


print(is_palindrome(input))
