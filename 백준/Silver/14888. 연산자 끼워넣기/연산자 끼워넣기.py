import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
A_li = list(map(int, input().strip().split()))
op_cnt = list(map(int, input().strip().split()))

Max = -1000000000
Min = 1000000000

def recursion(idx, res):
    global Max, Min
    if idx == N:
        Max = max(Max, res)
        Min = min(Min, res)
        return
    # 덧셈의 개수
    if op_cnt[0] > 0:
        op_cnt[0] -= 1
        recursion(idx + 1, res + A_li[idx])
        op_cnt[0] += 1
    if op_cnt[1] > 0:
        op_cnt[1] -= 1
        recursion(idx + 1, res - A_li[idx])
        op_cnt[1] += 1
    if op_cnt[2] > 0:
        op_cnt[2] -= 1
        recursion(idx + 1, res * A_li[idx])
        op_cnt[2] += 1
    if op_cnt[3] > 0:
        op_cnt[3] -= 1
        recursion(idx + 1, int(res / A_li[idx]))
        op_cnt[3] += 1

recursion(1, A_li[0])
print(Max)
print(Min)