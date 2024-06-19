import sys, heapq
input = sys.stdin.readline

N, H, T = map(int, input().split())
hp = []
count = 0
for _ in range(N):
    heapq.heappush(hp, -int(input()))

for _ in range(T):
    t = heapq.heappop(hp)
    if abs(t) < H:
        heapq.heappush(hp, abs(t) // 2)
        break
    elif abs(t) == 1:
        heapq.heappush(hp, abs(t))
    else:
        heapq.heappush(hp, -(abs(t) // 2))
        count += 1

if abs(min(hp)) < H:
    print("YES")
    print(count)
else:
    print("NO")
    print(abs(heapq.heappop(hp)))