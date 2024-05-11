from collections import deque

def BFS(start, graph, n):
    answer = [0] * (n + 1)
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[1] = True
    answer[1] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                answer[i] = answer[v] + 1
                q.append(i)
    return answer

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    answer = BFS(1, graph, n)
    
    cnt = 0
    MAX = max(answer)
    for i in answer:
        if i == MAX:
            cnt += 1
    return cnt