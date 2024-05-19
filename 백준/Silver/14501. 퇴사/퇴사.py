N = int(input())
t = []
p = []
dp = []
for _ in range(N):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)
    dp.append(P)

dp.append(0)
for i in range(N-1, -1, -1):
    if i + t[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
print(dp[0])