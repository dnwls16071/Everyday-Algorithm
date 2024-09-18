import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
MAX = -1000000000
MIN = 1000000000
# (+) (-) (x) (/)
op = list(map(int, input().split()))

def recursive(idx, res):
    global MAX, MIN
    if idx == N:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return 
    
    if op[0] > 0:
        op[0] -= 1
        recursive(idx + 1, res + A[idx])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        recursive(idx + 1, res - A[idx])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        recursive(idx + 1, res * A[idx])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        recursive(idx + 1, int(res / A[idx]))
        op[3] += 1           

recursive(1, A[0])
print(MAX)
print(MIN)