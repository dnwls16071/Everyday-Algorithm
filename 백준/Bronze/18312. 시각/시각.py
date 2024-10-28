import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 0
for h in range(N+1):
    if h < 10:
        h = '0' + str(h)
    for m in range(60):
        if m < 10:
            m = '0' + str(m)
        for s in range(60):
            if s < 10:
                s = '0' + str(s)
            if str(K) in str(h) or str(K) in str(m) or str(K) in str(s):
                result += 1
print(result)