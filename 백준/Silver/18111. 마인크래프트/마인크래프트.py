# 빈번하게 등장하는 값을 기준으로 맞추는 방법

# 블록 제거 -> 인벤토리에 넣는 것 : 2s
# 인벤토리에서 블록 하나를 꺼내 특정 좌표에 쌓기 : 1s

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
result = float('INF')   # 시간
level = 0               # 땅 높이

# 256 x 500 x 500 = 1억 밑
for h in range(257):
    u_cnt = 0
    nu_cnt = 0
    for y in range(N):
        for x in range(M):
            if maps[y][x] > h:
                nu_cnt += abs(maps[y][x] - h)
            else:
                u_cnt += abs(h - maps[y][x])
    
    # 인벤토리에 있는 블럭의 개수 B
    # nu_cnt : 고르게 하기 위해 빼야되는 블록의 개수
    # u_cnt : 고르게 하기 위해 추가해야되는 블록의 개수
    if B + nu_cnt < u_cnt:
        continue
    tc = nu_cnt * 2 + u_cnt

    if result >= tc:
        result = tc
        level = h

print(result, level)