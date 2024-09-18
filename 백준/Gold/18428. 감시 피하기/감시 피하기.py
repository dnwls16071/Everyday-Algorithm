import sys
input = sys.stdin.readline
from itertools import combinations

# 선생님의 감시(일직선 방향으로)    
def search(y, x, direction):
    if direction == 0:
        while y >= 0:
            if maps[y][x] == "S":
                return False
            if maps[y][x] == "O":
                return True
            y -= 1
    elif direction == 1:
        while x >= 0:
            if maps[y][x] == "S":
                return False
            if maps[y][x] == "O":
                return True
            x -= 1
    elif direction == 2:
        while y < N:
            if maps[y][x] == "S":
                return False
            if maps[y][x] == "O":
                return True
            y += 1
    elif direction == 3:
        while x < N:
            if maps[y][x] == "S":
                return False
            if maps[y][x] == "O":
                return True
            x += 1
    return True
            
def process():
    for ty, tx in teacher:
        for i in range(4):
            if not search(ty, tx, i):
                return False
    return True

# S : 학생, T : 선생님, O : 장애물
# 최대 : 36
# 전체 선생님의 수 5이하
# 전체 학생 수 30이하
N = int(input())
maps = [list(map(str, input().split())) for _ in range(N)]

student = []
teacher = []
empty = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == "S":
            student.append((i, j))
        elif maps[i][j] == "T":
            teacher.append((i, j))
        elif maps[i][j] == "X":
            empty.append((i, j))

flag = False
for comb in combinations(empty, 3):
    for cy, cx in comb:
        maps[cy][cx] = "O"
    if process():
        flag = True
        break
    for cy, cx in comb:
        maps[cy][cx] = "X"

if flag:
    print("YES")
else:
    print("NO")