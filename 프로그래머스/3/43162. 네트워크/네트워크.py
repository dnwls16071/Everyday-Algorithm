def solution(n, computers):
    visited = [False] * (n + 1)
    answer = 0
    def DFS(start):
        nonlocal visited, answer
        visited[start] = True
        for i in range(n):
            if not visited[i] and computers[start][i]:
                DFS(i)
        return answer
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    return answer