N, k = input().split()
score_list = list(map(int, list(input().split(" "))))
score_list.sort(key=lambda x: -x)

print(score_list[int(k) - 1])
