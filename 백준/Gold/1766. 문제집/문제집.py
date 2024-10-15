import sys, heapq
input = sys.stdin.readline

def topology_sort():
    h = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(h, i)
    
    while h:
        v = heapq.heappop(h)
        result.append(v)
        for i in seq[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(h, i)

N, M = map(int, input().split())
result = []
indegree = [0] * (N+1)
seq = [[] for _ in range(N+1)]      # zero base
for _ in range(M):
    a, b = map(int, input().split())    # zero base
    seq[a].append(b)
    indegree[b] += 1

topology_sort()
print(*result)