import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def BFS(a, b):
    q = deque()
    union = []
    q.append([a, b])
    union.append([a, b])
    visited[a][b] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(maps[ny][nx] - maps[y][x]) <= R:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    union.append([ny, nx])
    return union

answer = 0
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                u = BFS(i, j)
                if len(u) > 1:  # 연합이 존재한다면 인구 이동이 발생
                    flag = True
                    tot = 0         # 연합의 전체 인구 수
                    for uy, ux in u:
                        tot += maps[uy][ux]
                    average = int(tot / len(u))
                    for uy, ux in u:
                        maps[uy][ux] = average
                
    if flag:
        answer += 1
    else:
        print(answer)
        break