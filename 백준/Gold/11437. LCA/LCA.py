import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
parent = [i for i in range(N + 1)]
depth = [0 for _ in range(N + 1)]
visited = [False] * (N + 1)

def BFS(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                depth[i] = depth[v] + 1
                parent[i] = v
                q.append(i)

def LCA(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1)
M = int(input())
for _ in range(M):        
    m, n = map(int, input().split())
    print(LCA(m, n))