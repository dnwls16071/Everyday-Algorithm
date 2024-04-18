import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = int(1e9)
for comb in combinations(chicken, M):
    temp = 0
    for h in house:
        MAX_DISTANCE = int(1e9)
        for i in range(M):
            MAX_DISTANCE = min(MAX_DISTANCE, abs(h[0] - comb[i][0]) + abs(h[1] - comb[i][1]))
        temp += MAX_DISTANCE
    result = min(result, temp)
print(result)