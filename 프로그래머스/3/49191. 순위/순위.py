def solution(n, results):
    answer = 0
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for result in results:
        # a가 b를 이긴다.
        # 4번이 3번을 이기고 3번이 2번을 이긴다면 4번이 2번을 이긴다는 간접적 추론이 가능함
        a, b = result
        graph[a][b] = True
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    for a in range(1, n + 1):
        cnt = 0
        for b in range(1, n + 1):
            if a == b:
                continue
                
            if graph[a][b] or graph[b][a]:
                cnt += 1
        if cnt == n - 1:
            answer += 1
    return answer