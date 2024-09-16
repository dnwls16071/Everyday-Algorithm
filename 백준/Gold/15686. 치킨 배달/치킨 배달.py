import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

def calculate_distance():
    total = 0
    for h in house:
        dist = float('inf')
        for c in selected:
            dist = min(dist, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        total += dist
    return total

def recursive(idx, count):
    global answer
    if count == M:
        answer = min(answer, calculate_distance())
        return
    if idx == len(chicken):
        return
    
    selected.append(chicken[idx])
    recursive(idx + 1, count + 1)
    selected.pop()
    recursive(idx + 1, count)

selected = []
recursive(0, 0)
print(answer)