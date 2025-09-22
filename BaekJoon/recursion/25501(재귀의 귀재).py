N = int(input())


def is_palindrome(string, start_index, end_index, count):
    count += 1
    if start_index >= end_index:
        return 1, count
    if string[start_index] == string[end_index]:
        return is_palindrome(string, start_index + 1, end_index - 1, count)
    else:
        return 0, count


for i in range(N):
    string = input()
    result , count = is_palindrome(string, 0, len(string) - 1, 0)
    print(result, count)
