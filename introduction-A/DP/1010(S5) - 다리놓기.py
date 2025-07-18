def solve_bridge():
    # DP 테이블 초기화 (최대 30x30)
    dp = [[0] * 31 for _ in range(31)]

    # 초기값 설정
    # dp[i][j] = C(j, i) = j개 중에서 i개를 선택하는 경우의 수
    for i in range(31):
        dp[0][i] = 1  # 0개를 선택하는 경우의 수는 항상 1
        if i <= 30:
            dp[i][i] = 1  # i개 중에서 i개를 선택하는 경우의 수는 1

    # DP 테이블 채우기
    # dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    # 파스칼의 삼각형 원리 사용
    for i in range(1, 31):
        for j in range(i + 1, 31):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

    # 테스트 케이스 처리
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(dp[N][M])


# 실행
solve_bridge()