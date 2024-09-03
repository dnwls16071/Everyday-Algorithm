from collections import deque

def solution(maps):
    width = len(maps[0])
    height = len(maps)
    visited = [[False] * width for _ in range(height)]
    
    q = deque()
    q.append([0, 0, 1]) # 좌표값 + 지나간 칸 수
    visited[0][0] = True
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    while q:
        y, x, cnt = q.popleft()
        if y == height - 1 and x == width - 1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < height and 0 <= nx < width:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    q.append([ny, nx, cnt + 1])
                    visited[ny][nx] = True
    return -1
