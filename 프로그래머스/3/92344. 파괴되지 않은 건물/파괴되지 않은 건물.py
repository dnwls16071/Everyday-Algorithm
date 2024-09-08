def solution(board, skill):
    height, width = len(board), len(board[0])
    prefix = [[0] * (width + 1) for _ in range(height + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        degree *= -1 if type == 1 else 1
        prefix[r1][c1] += degree
        prefix[r1][c2 + 1] -= degree
        prefix[r2 + 1][c1] -= degree
        prefix[r2 + 1][c2 + 1] += degree
    
    # 가로 방향 누적 합
    for i in range(height + 1):
        for j in range(1, width + 1):
            prefix[i][j] += prefix[i][j-1]
    
    # 세로 방향 누적 합
    for j in range(width + 1):
        for i in range(1, height + 1):
            prefix[i][j] += prefix[i-1][j]
        
    tot = 0
    for i in range(height):
        for j in range(width):
            board[i][j] += prefix[i][j]
            if board[i][j] > 0:
                tot += 1
    return tot