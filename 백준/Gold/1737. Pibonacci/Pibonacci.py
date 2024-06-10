import math, sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pibonacci(n):
    if 0 <= n <= math.pi:
        return 1
    if n in memoization:
        return memoization[n]
    memoization[n] = pibonacci(n-1) + pibonacci(n-math.pi)
    return memoization[n] % 1000000000000000000

N = int(input())
memoization = {}
print(pibonacci(N))