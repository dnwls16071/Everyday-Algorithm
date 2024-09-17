import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        t = q.popleft()
        for i in graph[t]:
            if visited[i] == -1:
                visited[i] = visited[t] + 1
                q.append(i)

BFS(X)

result = []
for idx, v in enumerate(visited):
    if v == K:
        result.append(idx)

if len(result) > 0:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)