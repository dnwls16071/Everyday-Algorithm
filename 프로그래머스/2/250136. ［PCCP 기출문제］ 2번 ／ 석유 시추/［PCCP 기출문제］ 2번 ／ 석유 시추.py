from collections import deque

def solution(land):
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    array = [0] * 500

    def BFS(a, b):
        temp = set()
        q = deque()
        q.append((a, b))
        visited[a][b] = True
        temp.add(b)
        cnt = 1 # 한 덩어리 석유 매장량(시작 지점 포함)
        while q:
            y, x = q.popleft()
            dy = [1, 0, -1, 0]
            dx = [0, -1, 0, 1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < len(land) and 0 <= nx < len(land[0]):
                    if not visited[ny][nx] and land[ny][nx] == 1:
                        q.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1
                        temp.add(nx)
        
        for t in temp:
            array[t] += cnt
    
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
    return max(array)
    
    