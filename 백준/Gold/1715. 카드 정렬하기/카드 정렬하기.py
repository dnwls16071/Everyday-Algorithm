import sys, heapq
input = sys.stdin.readline

N = int(input())

card = []
for _ in range(N):
    heapq.heappush(card, int(input()))

tot = 0
while len(card) >= 2:
    f1 = heapq.heappop(card)
    f2 = heapq.heappop(card)
    tot += f1 + f2
    heapq.heappush(card, f1 + f2)
print(tot)    