from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

cnt = 0
for i in range(1, N+1):
    for j in combinations(arr, i):
        if sum(j) == S:
            cnt += 1
print(cnt)