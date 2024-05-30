import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
root = 0
dn = int(input())
cnt = 0

tree = [[] for _ in range(N)]
for p in range(N):
    if parent[p] == -1:
        root = p
    else:
        if p != dn:
            tree[parent[p]].append(p)

def DFS(node):
    global cnt
    if len(tree[node]) == 0:
        cnt += 1
    for i in range(len(tree[node])):
        if tree[node][i] == dn:
            if len(tree[node]) == 0:
                cnt += 1
        else:
            DFS(tree[node][i])

if root == dn:
    print(0)
else:
    DFS(root)
    print(cnt)