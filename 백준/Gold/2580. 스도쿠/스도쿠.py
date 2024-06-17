import sys
input = sys.stdin.readline

def chk_row(t, n):
    # t번째 가로줄에 n이란 숫자가 중복된다면 False, 중복되지않는다면 True
    for i in range(9):
        if board[t][i] == n:
            return False
    return True

def chk_col(t, n):
    # t번째 세로줄에 n이란 숫자가 중복된다면 False, 중복되지않는다면 True
    for i in range(9):
        if board[i][t] == n:
            return False
    return True

def chk_rect(y, x, n):
    for i in range(3):
        for j in range(3):
            if board[(y // 3) * 3 + i][(x // 3) * 3 + j] == n:
                return False
    return True

def solution(idx):
    if idx == len(el):
        for i in board:
            print(*i)
        exit(0)
    y = el[idx][0]
    x = el[idx][1]
    for i in range(1, 10):
        if chk_rect(y, x, i) and chk_row(y, i) and chk_col(x, i):
            board[y][x] = i
            solution(idx + 1)
            board[y][x] = 0    

board = [list(map(int, input().split())) for _ in range(9)]
el = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            el.append([i, j])
solution(0)