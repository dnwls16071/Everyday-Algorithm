import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def BFS(y, x):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    q = deque()
    q.append((y, x))
    union = [(y, x)]            # 연합 개수
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if abs(graph[ny][nx] - graph[y][x]) >= L and abs(graph[ny][nx] - graph[y][x]) <= R:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    union.append((ny, nx))
    return union

result = 0  # 인구 이동이 발생하는 횟수
while True:
    flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                union = BFS(i, j)

                if len(union) > 1:
                    flag = True
                    for u in union:
                        y, x = u
                        value = sum(graph[y][x] for y, x in union) // len(union)
                    for u in union:
                        y, x = u
                        graph[y][x] = value
    if not flag: 
        break
    else:
        result += 1
print(result)