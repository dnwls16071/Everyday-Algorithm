import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = []
for _ in range(N):
    lst = list(map(int, input().split()))
    arr1.append(lst)

M, K = map(int, input().split())
arr2 = []
for _ in range(M):
    lst = list(map(int, input().split()))
    arr2.append(lst)

result = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += arr1[i][k] * arr2[k][j]

for i in result:
    print(*i)