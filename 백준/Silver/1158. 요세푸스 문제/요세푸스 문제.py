from collections import deque
import sys

N, K = map(int, sys.stdin.readline().strip().split())
queue = deque()
for i in range(1, N+1):
    queue.append(i)

result = []
for i in range(N):
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end = "")
print(*result, sep = ", ", end = "")
print(">")