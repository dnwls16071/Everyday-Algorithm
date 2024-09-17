import sys, copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

empty = []
wall = []
virus = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty.append((i, j))
        elif maps[i][j] == 1:
            wall.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))

def BFS(a, b, cp):
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    while q:
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if cp[ny][nx] == 0:
                    cp[ny][nx] = 2
                    visited[ny][nx] = True
                    q.append((ny, nx))

answer = float('inf') * (-1)
for comb in combinations(empty, 3):
    cp = copy.deepcopy(maps)
    for cy, cx in comb:
        cp[cy][cx] = 1
    for vy, vx in virus:
        BFS(vy, vx, cp)    
    result = 0
    for line in cp:
        result += line.count(0)
    answer = max(answer, result)
print(answer)