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

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for j in range(1, N+1):
        if lst[j-1] == 1:
            union(i, j)
vp = list(map(int, input().split()))

value = find(vp[0])
for i in range(M):
    if find(vp[i]) != value:
        print("NO")
        break
else:
    print("YES")