from collections import deque

def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    maps = [list(map(str, x)) for x in maps]
    # 숫자 처리
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X":
                maps[i][j] = int(maps[i][j])

    # BFS
    def BFS(a, b):
        q = deque()
        q.append((a, b))
        area = maps[a][b]
        visited[a][b] = True
        dy = [-1, 0, 1, 0]
        dx = [0, -1, 0, 1]
        while q:
            y, x = q.popleft()  
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                    if not visited[ny][nx] and maps[ny][nx] != "X":
                        q.append((ny, nx))
                        area += maps[ny][nx]
                        visited[ny][nx] = True
        return area  

    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not visited[i][j] and maps[i][j] != "X":
                answer.append(BFS(i,j))
    if len(answer):
        answer.sort()
        return answer
    else:
        return [-1]