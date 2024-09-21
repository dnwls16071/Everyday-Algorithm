import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)  # 최대 수익 배열

# 뒤에서부터 접근하는 방법을 선택
for i in range(N-1, -1, -1):
    # 퇴사 일정을 넘어서게 되면 상담을 할 수 없게 됨
    if T[i] + i > N:
        dp[i] = dp[i+1]        
    else:
        dp[i] = max(dp[i+1], dp[i + T[i]] + P[i])
print(dp[0])