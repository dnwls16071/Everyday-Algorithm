def DFS(n, graph, visited):
    visited[n] = True
    for i in range(len(graph[n])):
        if not visited[i] and graph[n][i] == 1:
            DFS(i, graph, visited)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(len(computers)):
        if not visited[i]:
            DFS(i, computers, visited)
            answer += 1
    return answer