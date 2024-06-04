import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
room = [input().strip() for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]

def BFS(y, x):
    q = deque()
    q.append([y, x])
    visited[y][x] = 0
    while q:
        y, x = q.popleft()
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        if y == N-1 and x == N-1:
            break
        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
                    # 흰 방이라면? -> 우선적으로 탐색하기위해 appendleft()
                    if room[ny][nx] == "1":
                        visited[ny][nx] = visited[y][x]
                        q.appendleft([ny, nx])
                    # 검은 방이라면? -> 흰 방으로 바꾸어야하므로 바꾸어야 할 방의 개수를 1만큼 증가
                    else:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append([ny, nx])

BFS(0, 0)
print(visited[N-1][N-1])