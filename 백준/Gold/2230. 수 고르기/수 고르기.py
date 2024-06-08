import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

INF = int(2e9)
p1 = 0; p2 = 0
arr.sort()
while p2 < len(arr):
    temp = arr[p2] - arr[p1]
    if temp > M:
        p1 += 1
        INF = min(INF, temp)
    elif temp < M:
        p2 += 1
    else:
        INF = M
        print(INF)
        exit(0)
print(INF)