bingo = []
answer = []
isRevealed = []


def findNum(lists, a):
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if lists[i][j] == a:
                return i, j
    return None


def isBingo(lists):
    count = 0
    for i in range(len(lists)):
        if i == 0:
            if lists[0][0] == 1 & lists[1][1] == 1 & lists[2][2] == 1 & lists[3][3] == 1 & lists[4][4] == 1:
                count += 1
        if i == 4:
            if lists[0][4] == 1 & lists[1][3] == 1 & lists[2][2] == 1 & lists[3][1] == 1 & lists[4][0] == 1:
                count += 1
        if lists[i][0] == 1 & lists[i][1] == 1 & lists[i][2] == 1 & lists[i][3] == 1 & lists[i][4] == 1:
            count += 1
        if lists[0][i] == 1 & lists[1][i] == 1 & lists[2][i] & lists[3][i] == 1 & lists[4][i] == 1:
            count += 1
    return count


def test(bingo2):
    counts = 0
    for i in range(5):
        lines = list(map(int, input().split()))
        for j in range(5):
            counts += 1
            a, b = findNum(bingo2, lines[j])
            isRevealed[a][b] = 1
            if isBingo(isRevealed) >= 3:
                return counts
    return counts


for i in range(5):
    line = list(map(int, input().split()))
    bingo.append(line)
    isRevealed.append([0, 0, 0, 0, 0])
print(test(bingo))