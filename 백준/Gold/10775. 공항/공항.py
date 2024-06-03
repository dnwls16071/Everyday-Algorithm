import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

G = int(input())
P = int(input())
airplane = []
for _ in range(P):
    g = int(input())
    airplane.append(g)

parent = [i for i in range(G+1)]
cnt = 0
for ap in airplane:
    x = find(ap)
    if x == 0:
        break
    parent[x] = parent[x-1]
    cnt += 1
print(cnt)