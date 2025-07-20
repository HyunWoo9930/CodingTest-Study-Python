T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    n = int(input())  # 숫자 개수
    nums = list(map(int, input().split(" ")))
    nums_with_index = []
    bools = [0] * n
    for i in range(n):
        nums_with_index.append([i + 1, nums[i]])
    count = 0
    for i in range(n):
        if bools[i] == 1:
            continue
        bools[i] = 1
        target = nums_with_index[i][0]
        num = nums_with_index[i][1]
        while 1:
            bools[num - 1] = 1
            if target == num:
                break
            num = nums_with_index[num - 1][1]
        count += 1
    print(count)
