input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    index = 3
    while index <= n:
        fibo_memo[index] = fibo_memo.get(index-1) + fibo_memo.get(index-2)
        index += 1
    return fibo_memo.get(n)


print(fibo_dynamic_programming(input, memo))
