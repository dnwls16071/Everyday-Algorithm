import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    dp = [[0] * 11 for _ in range(65)]
    dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    n = int(input())
    if n == 1:
        print(10)
        continue
    for i in range(2, n+1):
        for j in range(11):
            # 전체 개수
            if j == 10:
                dp[i][10] = sum(dp[i])
            elif j == 0:
                dp[i][0] = dp[i-1][10]
            else:
                dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
    print(dp[n][10])