import sys, heapq
input = sys.stdin.readline

n = int(input())
lst = []; heap = []
for i in range(n):
    p, d = map(int, input().split())
    lst.append((d, p))
lst.sort()

for d, p in lst:
    heapq.heappush(heap, p)
    if len(heap) > d:
        heapq.heappop(heap)
print(sum(heap))