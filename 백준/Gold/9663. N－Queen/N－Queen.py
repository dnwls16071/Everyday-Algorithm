import sys
input = sys.stdin.readline

N = int(input())
row = [0] * N
result = 0

def attackable(r):
    # 현재까지 놓은 퀸의 개수만큼 반복문
    for i in range(r):
        # 같은 라인 불가
        if row[i] == row[r]:
            return False
        # 대각선 불가
        if abs(row[i] - row[r]) == abs(i - r):
            return False
    return True

def solution(r):
    global result
    if r == N:
        result += 1
        return
    for i in range(N):
        row[r] = i
        if attackable(r):
            solution(r+1)

solution(0)
print(result)