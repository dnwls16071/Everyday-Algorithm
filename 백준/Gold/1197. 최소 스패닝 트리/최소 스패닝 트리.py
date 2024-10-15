import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()
result = 0
for e in edges:
    cost, a, b = e
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)