import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append((i, j))
        elif maps[i][j] == 2:
            chicken.append((i, j))

def recursive(picked, idx):
    global answer
    # 백트래킹 종료 조건 : 최대 M개의 치킨집을 골랐다면?
    # 치킨 배달 최소거리 합 구하기
    if len(picked) == M:
        tot = 0 # 치킨 배달 합
        for hy, hx in house:
            standard = float('inf')
            for cy, cx in picked:
                dist = abs(hy - cy) + abs(hx - cx)
                standard = min(standard, dist)
            tot += standard
        answer = min(answer, tot)
        return
    for i in range(idx, len(chicken)):
        picked.append(chicken[i])
        recursive(picked, i+1)
        picked.pop()

picked = []
recursive([], 0)
print(answer)