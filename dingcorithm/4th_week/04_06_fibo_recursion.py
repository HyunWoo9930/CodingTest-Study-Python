input = 20


def fibo_recursion(n):
    if n == 0 or n == 1:
        return n
    return fibo_recursion(n - 2) + fibo_recursion(n - 1)


print(fibo_recursion(input))  # 6765