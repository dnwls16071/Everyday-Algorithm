from collections import deque
from itertools import combinations
import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
MAX =  -1   # 안전 영역 최대 크기
graph = []  # 전체 지도 정보
for _ in range(N):
    graph.append(list(map(int, input().split())))
"""
0 : 빈 칸
1 : 벽
2 : 바이러스
"""
virus = []      # 바이러스가 있는 좌표의 정보
empties = []    # 빈 칸이 있는 좌표의 정보
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            empties.append([i, j])

def BFS():
    global MAX
    for comb in combinations(empties, 3):
        cg = copy.deepcopy(graph)
        for y, x in comb:
            cg[y][x] = 1
        
        cnt = 0
        q = deque(virus)
        while q:
            y, x = q.popleft()
            dy = [1, 0, -1, 0]
            dx = [0, 1, 0, -1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue            
                if 0 <= ny < N and 0 <= nx < M:
                    if cg[ny][nx] == 0:
                        cg[ny][nx] = 2
                        q.append([ny, nx])

        for i in range(N):
            for j in range(M):
                if cg[i][j] == 0:
                    cnt += 1
        MAX = max(MAX, cnt)
    return MAX

result = BFS()
print(result)