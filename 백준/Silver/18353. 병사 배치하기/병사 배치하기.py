import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [1] * (N + 1)  # 병사 전투 배치 현황

for i in range(1, N):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))