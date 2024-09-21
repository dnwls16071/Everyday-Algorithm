import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))
dp = [1] * (N+1)

for i in range(1, N):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))