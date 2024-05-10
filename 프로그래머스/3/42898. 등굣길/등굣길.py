def solution(m, n, puddles):
    info = [[0] * (m+1) for _ in range(n+1)]
    info[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                info[i][j] = 0
            else:
                info[i][j] = (info[i-1][j] + info[i][j-1]) % 1000000007
    return info[-1][-1]