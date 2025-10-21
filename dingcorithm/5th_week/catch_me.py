# Q. 연인 코니와 브라운은 광활한 들판에서 ‘나 잡아 봐라’ 게임을 한다.
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다.
# 게임이 끝나는데 걸리는 최소 시간을 구하시오.
#
# 조건은 다음과 같다.
# 코니는 처음 위치 C에서 1초 후 1만큼 움직이고,
# 이후에는 가속이 붙어 매 초마다 이전 이동 거리 + 1만큼 움직인다.
# 즉 시간에 따른 코니의 위치는 C, C + 1, C + 3, C + 6, …이다.
#
# 브라운은 현재 위치 B에서 다음 순간 B – 1, B + 1, 2 * B 중 하나로 움직일 수 있다.
# 코니와 브라운의 위치 p는 조건 0 <= x <= 200,000을 만족한다.
# 브라운은 범위를 벗어나는 위치로는 이동할 수 없고, 코니가 범위를 벗어나면 게임이 끝난다
#

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    step = 0
    queue = deque()
    queue.append(brown_loc - 1)
    queue.append(brown_loc + 1)
    queue.append(brown_loc * 2)

    print(queue)
    while cony_loc < 200000:
        prev_cony_loc = cony_loc
        cony_loc = next_c(prev_cony_loc, step)
        length = len(queue)
        for i in range(length):
            prev_brown_loc = queue.popleft()
            if prev_brown_loc - 1 >= cony_loc or prev_brown_loc + 1 >= cony_loc or prev_brown_loc * 2 >= cony_loc:
                return step
            queue.append(brown_loc - 1)
            queue.append(brown_loc + 1)
            queue.append(brown_loc * 2)
            message = 'adadas'
            message.re

        step += 1
    return step


def next_c(prev, step):
    return prev + step + 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))
