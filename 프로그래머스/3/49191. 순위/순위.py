def solution(n, results):
    result = [[0] * (n + 1) for _ in range(n + 1)]
    for r in results:
        a, b = r    # a가 b를 이긴다.
        result[a][b] = 1
    
    # 플로이드
    for k in range(1, n+1):             # 경유
        for a in range(1, n+1):         # 시작
            for b in range(1, n+1):     # 도착
                if result[a][k] == 1 and result[k][b] == 1:
                    result[a][b] = 1
    
    answer = 0  # 정확한 순위를 알 수 있는 선수의 수
    for i in range(len(result)):
        cnt = 0
        for j in range(len(result[i])):
            if result[i][j] == 1 or result[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer