from collections import deque

def solution(maps):
    board = []
    for m in maps:
        board.append(list(m))

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            # 시작 지졈
            if maps[i][j] == "S":
                sy, sx = i, j
            # 레버 지점
            if maps[i][j] == "L":
                ly, lx = i, j
            # 출구 지점
            if maps[i][j] == "E":
                ey, ex = i, j
                
    def BFS(sy, sx, ty, tx, cnt):
        q = deque()
        q.append([sy, sx, 0])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[sy][sx] = True
        while q:
            y, x, cnt = q.popleft()
            if y == ty and x == tx:
                return cnt
            dy = [1, 0, -1, 0]
            dx = [0, 1, 0, -1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                    if maps[ny][nx] != "X":
                        visited[ny][nx] = True
                        q.append([ny, nx, cnt + 1])
        return -1
    p1 = BFS(sy, sx, ly, lx, 0)
    p2 = BFS(ly, lx, ey, ex, 0)
    if p1 == -1 or p2 == -1:
        return -1
    else:
        return p1 + p2