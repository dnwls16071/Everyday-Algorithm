import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
        
def union(x, y):
    x = find(x)
    y = find(y)
    if fc[x] < fc[y]:
        parent[y] = x
    else:
        parent[x] = y

N, M, k = map(int, input().split())
fc = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)

friends = set()
mc = 0
for i in range(1, N+1):
    if find(i) not in friends:
        friends.add(find(i))
        mc += fc[find(i)]

if k < mc:
    print("Oh no")
else:
    print(mc)