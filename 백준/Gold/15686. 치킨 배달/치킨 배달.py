import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
Map = [list(map(int, input().strip().split())) for _ in range(N)]

chicken = []          # 치킨집 리스트
house = []              # 집 리스트
choosen_chicken = []    # 선택된 치킨집 리스트
for i in range(N):
    for j in range(N):
        if Map[i][j] == 2:
            chicken.append((i, j))
        elif Map[i][j] == 1:
            house.append((i, j))

answer = 10000000
def recursive(level, idx):
    global answer
    if level == M:
        chicken_distance = 0
        for h in house:
            dist = 10000000
            for ch in choosen_chicken:
                tmp = abs(h[0] - ch[0]) + abs(h[1] - ch[1])
                dist = min(dist, tmp)
            chicken_distance += dist
        answer = min(answer, chicken_distance)
        return answer
    for i in range(idx, len(chicken)):
        if chicken[i] in choosen_chicken:
            continue
        choosen_chicken.append(chicken[i])
        recursive(level+1, i+1)
        choosen_chicken.pop()

recursive(0, 0)
print(answer)