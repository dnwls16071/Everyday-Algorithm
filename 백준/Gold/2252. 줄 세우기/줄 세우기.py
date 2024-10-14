import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)
    
    while q:
        v = q.popleft()
        for i in seq[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                result.append(i)

N, M = map(int, input().split())
data = [i for i in range(N+1)]   # zero base 
indegree = [0] * (N+1)         # zero base
seq = [[] for _ in range(N+1)]   # zero base

result = []
for _ in range(M):
    a, b = map(int, input().split())
    seq[a].append(b)
    indegree[b] += 1

topology_sort()
print(*result)