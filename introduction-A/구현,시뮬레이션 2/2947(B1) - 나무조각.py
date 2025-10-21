def test(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            print(list[0], list[1], list[2], list[3], list[4])

def test2(list):
    for i in range(len(list)):
        if list[i] != i:
            test(list)
lists = list(map(int, input().split(" ")))

test2(lists)
