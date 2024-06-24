from collections import deque
import sys
input = sys.stdin.readline

X, K = map(int, input().split())
LIMIT = 500000
# visited[pos][0] : 수빈이가 홀수 초에 도착
# visited[pos][1] : 수빈이가 짝수 초에 도착
visited = [[False] * 2 for _ in range(LIMIT + 1)]

def BFS():
    global K
    if X == K:
        print(0)
        sys.exit(0)
    q = deque()
    q.append(X)
    time = 1
    K += time
    
    while True:
        if K > LIMIT:
            print(-1)
            break
        nq = deque()
        
        while q:
            v = q.popleft()
            for p in [v-1, v+1, v*2]:
                if 0 <= p <= LIMIT and not visited[p][time % 2]:
                    visited[p][time % 2] = time
                    nq.append(p)

        if visited[K][time % 2]:
            print(time)
            sys.exit(0)
        time += 1
        K += time
        q = nq
BFS()