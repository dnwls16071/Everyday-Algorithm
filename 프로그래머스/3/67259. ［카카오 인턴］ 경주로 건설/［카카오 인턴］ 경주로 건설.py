from collections import deque

def solution(board):
    def bfs(y, x, cost, path):
        length = len(board)
        visited = [[987654321] * length for _ in range(length)]
        visited[y][x] = 0

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        q = deque()
        q.append([y, x, cost, path])
        while q:
            y, x, cost, path = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < length and 0 <= nx < length and board[ny][nx] == 0:
                    if i == path: 
                        newcost = cost + 100
                    else: 
                        newcost = cost + 600
                    if newcost < visited[ny][nx]:
                        visited[ny][nx] = newcost
                        q.append([ny, nx, newcost, i])
        return visited[-1][-1]
    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 2))