import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, M):
    dp[0][i] += dp[0][i-1]

for i in range(1, N):
    ltr = dp[i][:]
    rtl = dp[i][:]
    # 왼쪽에서 오른쪽으로
    # #1. 왼쪽에서 오른쪽으로 가는 경우
    # #2. 위쪽에서 아래쪽으로 가는 경우
    for j in range(M):
        # 위에서 아래로 내려오는 경우
        if j == 0:
            ltr[j] += dp[i-1][j]
        else:
            ltr[j] = ltr[j] + max(ltr[j-1], dp[i-1][j])
    
    # 오른쪽에서 왼쪽으로
    # #1. 오른쪽에서 왼쪽으로 가는 경우
    # #2. 위쪽에서 아래쪽으로 가는 경우
    for j in range(M-1, -1, -1):
        # 위에서 아래로 내려오는 경우
        if j == M-1:
            rtl[j] += dp[i-1][j]
        else:
            rtl[j] = rtl[j] + max(rtl[j+1], dp[i-1][j])
    
    for j in range(M):
        dp[i][j] = max(ltr[j], rtl[j])
print(dp[N-1][M-1])