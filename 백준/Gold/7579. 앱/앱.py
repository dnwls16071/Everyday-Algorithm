import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memory = [0] + list(map(int, input().split()))
bytes = [0] + list(map(int, input().split()))

dp = [[0] * (sum(bytes) + 1) for _ in range(N + 1)]

answer = sum(bytes)

for i in range(1, N+1):
    m = memory[i]
    b = bytes[i]
    for j in range(sum(bytes) + 1): 
        if j < b:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-b] + m)
        
        if dp[i][j] >= M:
            answer = min(answer, j)
print(answer)