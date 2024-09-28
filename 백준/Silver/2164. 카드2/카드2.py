import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque(i for i in range(N, 0, -1))

while len(q) != 1:
    q.pop()
    val = q.pop()
    q.appendleft(val)
print(q[0])