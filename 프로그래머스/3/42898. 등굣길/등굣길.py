def solution(m, n, puddles):
    map = [[0] * m for _ in range(n)]
    map[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles or (i == 0 and j == 0):
                continue
            map[i][j] = (map[i-1][j] + map[i][j-1]) % 1000000007
    return map[-1][-1]