import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

MAX = -int(1e9)
MIN = int(1e9)

def DFS(curr, idx):
    global add, sub, mul, div, MAX, MIN
    if idx == N:
        MAX = max(MAX, curr)
        MIN = min(MIN, curr)
    else:
        if add > 0:
            add -= 1
            DFS(curr + A[idx], idx+1)
            add += 1
        if sub > 0:
            sub -= 1
            DFS(curr - A[idx], idx+1)
            sub += 1
        if mul > 0:
            mul -= 1
            DFS(curr * A[idx], idx+1)
            mul += 1
        if div > 0:
            div -= 1
            if curr < 0:
                DFS(-(abs(curr) // A[idx]), idx+1)
            else:
                DFS(abs(curr) // A[idx], idx+1)
            div += 1

DFS(A[0], 1)
print(MAX)
print(MIN)