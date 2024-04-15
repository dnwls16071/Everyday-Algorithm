import sys, copy
input = sys.stdin.readline
from itertools import combinations

N = int(input())
graph = [list(map(str, input().split())) for _ in range(N)]

teacher = []
obstacle = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == "T":
            teacher.append((i, j))
        elif graph[i][j] == "X":
            obstacle.append((i, j))

def search(y, x, direction, graph):
    # 위쪽 검사
    if direction == 0:
        while y > -1:
            if graph[y][x] == "S":
                return True
            if graph[y][x] == "O":
                return False
            y -= 1
    # 오른쪽 검사
    if direction == 1:
        while x < N:
            if graph[y][x] == "S":
                return True
            if graph[y][x] == "O":
                return False
            x += 1
    # 아래 검사
    if direction == 2:
        while y < N:
            if graph[y][x] == "S":
                return True
            if graph[y][x] == "O":
                return False
            y += 1
    # 왼쪽 검사
    if direction == 3:
        while x > -1:
            if graph[y][x] == "S":
                return True
            if graph[y][x] == "O":
                return False
            x -= 1
    return False

# 선생님 기준으로 상하좌우 방향 일직선 탐색
def linear(board):
    for i in teacher:
        ty, tx = i
        for i in range(4):
            if search(ty, tx, i, board):
                return True
    return False

find = False    # 애들이 전부 감시로부터 피할 수 있는지
for comb in combinations(obstacle, 3):
    temp = copy.deepcopy(graph)
    for y, x in comb:
        temp[y][x] = "O"
    
    if not linear(temp):
        find = True 
        break

if find:
    print("YES")
else:
    print("NO")