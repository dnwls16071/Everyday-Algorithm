import sys
sys.setrecursionlimit(10**6)

def recur(num, cnt):
    if num == 1:
        return cnt
    if cnt == 500:
        return -1
    
    if num % 2 == 0:
        return recur(num // 2, cnt + 1)
    else:
        return recur(num * 3 + 1, cnt + 1)

def solution(num):
    return recur(num, 0)
