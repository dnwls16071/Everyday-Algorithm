import sys
from collections import deque

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

N = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]
dic = dict()

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    graph[y][x] = 2

L = int(input())
for _ in range(L):
    s, dir = map(str, input().split())
    s = int(s)
    dic[s] = dir

direction = 0   # 맨 처음은 오른쪽
time = 0
y, x = 1, 1
graph[y][x] = 1
snakes = deque([(1, 1)])

def turn(alpha):
    global direction
    if alpha == "D":
        direction = (direction + 1) % 4
    else:
        if direction == 0:  # 오른쪽에서 왼쪽으로 회전(=위쪽)
            direction = 3
        else:
            direction = (direction - 1) % 4

def BFS():
    global direction, time, snakes, y, x
    while snakes:
        ny = y + dy[direction]
        nx = x + dx[direction]
        if ny <= 0 or ny > N or nx <= 0 or nx > N or (ny, nx) in snakes:
            break
        if graph[ny][nx] != 2:
            tail_y, tail_x = snakes.popleft()
            graph[tail_y][tail_x] = 0  # 꼬리 제거

        y, x = ny, nx
        graph[y][x] = 1
        snakes.append((ny, nx))
        time += 1

        if time in dic.keys():
            turn(dic[time])
    return time + 1

print(BFS())