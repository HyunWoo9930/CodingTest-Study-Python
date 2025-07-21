N, K = input().split()
N = int(N)
K = int(K)

pick = []
for i in range(N):
    pick.append([i, int(input())])

n = 0
count = 1
duplicate = []
isDuplicate = False
while pick[n][1] != K:
    if duplicate.__contains__(pick[n][0]):
        isDuplicate = True
        break
    duplicate.append(pick[n][0])
    n = pick[n][1]
    count += 1
if isDuplicate:
    print(-1)
else:
    print(count)
