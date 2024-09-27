import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 상어 초기 위치
for h in range(N):
    for w in range(N):
        if maps[h][w] == 9:
            by = h; bx = w
            break
# 초기 상어 크기
shark = 2

def BFS(a, b):
    distance = [[0] * N for _ in range(N)]      # 시간 당 최대 이동
    visited = [[False] * N for _ in range(N)]   # 방문 여부
    q = deque()
    q.append((a, b))
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    lst = []
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 방문하지 않은 곳이면서 자신의 크기보다 큰 물고기가 아니라면
                if maps[ny][nx] <= shark:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    # 0 : 빈 칸 제외 + 아기 상어 크기보다 작아야 가능
                    if maps[ny][nx] < shark and maps[ny][nx] != 0:
                        lst.append([ny, nx, distance[ny][nx]])
    # 거리가 가까운 물고기부터
    # 그 다음은 가장 위에 있는 물고기부터
    # 또 그 다음은 가장 왼쪽에 있는 물고기부터
    return sorted(lst, key=lambda x : (-x[2], -x[0], -x[1]))

time = 0    # 시간
cnt = 0     # 먹은 물고기 수
while True:
    s = BFS(by, bx)

    # 엄마 상어에게 도움을 요청
    if len(s) == 0:
        break
    cy, cx, distance = s.pop()
    time += distance
    maps[cy][cx] = maps[by][bx] = 0
    cnt += 1
    if cnt == shark:
        shark += 1
        cnt = 0
    maps[cy][cx] = 0
    by, bx = cy, cx
print(time)