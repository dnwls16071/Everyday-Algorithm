from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b):
    q = deque()
    q.append([a, b])
    while q:
        nx, ny = q.popleft()
        if abs(nx - rfx) + abs(ny - rfy) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                if abs(nx - cs[i][0]) + abs(ny - cs[i][1]) <= 1000:
                    visited[i] = True
                    q.append([cs[i][0], cs[i][1]])
    print("sad")
    return 

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    cs = []
    visited = [False for _ in range(n)]
    for _ in range(n):
        cx, cy = map(int, input().split())
        cs.append((cx, cy))
    rfx, rfy = map(int, input().split())
    BFS(hx, hy)