from collections import deque
import sys
input = sys.stdin.readline

N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수

maps = [[0] * (N + 1) for _ in range(N + 1)]        
y, x = 1, 1
maps[y][x] = 1
d = 0
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for _ in range(K):
    a, b = map(int, input().split())                                    # 사과 위치                         
    maps[a][b] = 2

L = int(input())                                                        # 뱀의 방향 전환 정보
info = {}
for _ in range(L):                                                                  
    X, C = map(str, input().split())
    info[int(X)] = C

time = 0
snake = deque([(1, 1)])
while True:
    ny = y + dy[d]
    nx = x + dx[d]
    # 벽에 부딪히거나 자기 자신에게 닿는 경우면 스탑
    if ny <= 0 or ny > N or nx <= 0 or nx > N or (ny, nx) in snake:
        break
    # 유효한 범위 내에 있다면
    if 0 < ny <= N and 0 < nx <= N:
        # 이동한 지점이 사과가 아니라면 위치를 바꿔줘야함
        if maps[ny][nx] != 2:
            a, b = snake.popleft()
            maps[a][b] = 0
        # 이동한 지점에 사과가 있다면 몸통을 늘려줘야 함
        y, x = ny, nx
        maps[ny][nx] = 1
        snake.append((ny, nx))
        time += 1
    
    # L : 왼쪽으로 90도 회전, D : 오른쪽으로 90도 회전
    if time in info.keys():
        if info[time] == 'L':
            if d == 0:
                d = (3 - d) % 4
            else:
                d -= 1
        else:
            if d == 3:
                d = (d + 1) % 4
            else:
                d += 1
print(time + 1)