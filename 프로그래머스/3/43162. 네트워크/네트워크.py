def solution(n, computers):
    visited = [False] * (n + 1)
    answer = 0
    def DFS(start):
        nonlocal visited, answer
        visited[start] = True
        for i in range(n):
            # 해당 노드에 방문한 적 없으면서 이전에 출발한 노드와 인접한 경우라면(1)?
            if not visited[i] and computers[start][i]:
                DFS(i)
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    return answer