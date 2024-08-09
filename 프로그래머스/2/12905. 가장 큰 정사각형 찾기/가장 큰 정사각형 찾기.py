def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1
    
    MAX = 0
    for i in board:
        MAX = max(max(i), MAX)
    return MAX * MAX