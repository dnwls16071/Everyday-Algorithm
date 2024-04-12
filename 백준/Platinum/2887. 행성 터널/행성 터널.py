import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

location = []
# i는 행성의 번호(루트 노드 찾을 때 쓰려고)
for i in range(N):
    a, b, c = map(int, input().split())
    location.append((a, b, c, i))

loc_x = sorted(location, key=lambda x : x[0])
loc_y = sorted(location, key=lambda x : x[1])
loc_z = sorted(location, key=lambda x : x[2])

edges = []
# edge = (distance, node1, node2)
for i in range(N-1):
    edge = ((abs(loc_x[i][0] - loc_x[i+1][0])), loc_x[i][3], loc_x[i+1][3]) 
    edges.append(edge)
for i in range(N-1):
    edge = ((abs(loc_y[i][1] - loc_y[i+1][1])), loc_y[i][3], loc_y[i+1][3])
    edges.append(edge)
for i in range(N-1):
    edge = ((abs(loc_z[i][2] - loc_z[i+1][2])), loc_z[i][3], loc_z[i+1][3])
    edges.append(edge)

edges.sort()    

total = 0
for edge in edges:
    distance, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        total += distance
print(total)