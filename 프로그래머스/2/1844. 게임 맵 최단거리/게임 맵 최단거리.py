from collections import deque

def solution(maps):
    X = len(maps[0])
    Y = len(maps)
    visited = [[0] * X for _ in range(Y)]
    
    def BFS(a, b):
        nonlocal X, Y
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        q = deque()
        q.append([a, b])
        visited[a][b] = 1
        while q:
            y, x = q.popleft()
            if y == Y - 1 and x == X - 1:
                return visited[y][x]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < Y and 0 <= nx < X:
                    if not visited[ny][nx] and maps[ny][nx]:
                        q.append([ny, nx]) 
                        visited[ny][nx] = visited[y][x] + 1
        return -1
    return BFS(0, 0)