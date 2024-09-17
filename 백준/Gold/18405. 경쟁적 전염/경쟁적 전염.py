import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 번호가 낮은 바이러스부터 먼저 증식(오름차순 정렬)
data = []
for i in range(N):
    for j in range(N):
        if maps[i][j] != 0:
            data.append([maps[i][j], i, j, 0])

data.sort()
q = deque(data)

def BFS():
    while q:
        types, y, x, s = q.popleft()
        if s == S:
            break
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if 0 <= ny < N and 0 <= nx < N:
                if maps[ny][nx] == 0:
                    maps[ny][nx] = types
                    q.append([types, ny, nx, s+1])

BFS()
if maps[X-1][Y-1] == 0:
    print(0)
else:
    print(maps[X-1][Y-1])