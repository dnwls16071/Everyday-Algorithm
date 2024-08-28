import sys
sys.setrecursionlimit(10**6)

def fibo(n, memoization):
    if n < 2:
        return 1
    if not memoization[n]:
        memoization[n] = fibo(n-1, memoization) + fibo(n-2, memoization)
    return memoization[n]

def solution(n):
    memoization = [0] * n
    memoization[0] = 1
    memoization[1] = 1
    fibo(n-1, memoization)
    return memoization[-1] % 1234567