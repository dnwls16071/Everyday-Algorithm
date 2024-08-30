from collections import deque

def solution(n, edge):
    route = [0] * (n + 1)
    route[1] = 1
    graph = [[] for _ in range(n + 1)]
    for v in edge:
        a, b = v
        graph[a].append(b)
        graph[b].append(a)
    
    def BFS():
        q = deque()
        q.append(1)
        while q:
            v = q.popleft()
            for i in graph[v]:
                if not route[i]:
                    route[i] = route[v] + 1
                    q.append(i)
    
    BFS()
    MAX = max(route)
    cnt = 0
    for i in route:
        if i == MAX:
            cnt += 1
    return cnt