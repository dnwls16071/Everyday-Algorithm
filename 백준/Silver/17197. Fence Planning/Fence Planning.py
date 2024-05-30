import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

N, M = map(int, input().split())
cows = []
for i in range(N):
    x, y = map(int, input().split())
    cows.append([x, y])

connections = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

def find_network(node, network):
    network.add(node)
    for neighbor in connections[node]:
        if neighbor not in network:
            find_network(neighbor, network)

networks = []
visited = set()
for cow in range(1, N + 1):
    if cow not in visited:
        network = set()
        find_network(cow, network)
        networks.append(network)
        visited.update(network)

min_perimeter = float('inf')
for network in networks:
    min_x = min(cows[cow - 1][0] for cow in network)
    max_x = max(cows[cow - 1][0] for cow in network)
    min_y = min(cows[cow - 1][1] for cow in network)
    max_y = max(cows[cow - 1][1] for cow in network)
    perimeter = 2 * (max_x - min_x + max_y - min_y)
    min_perimeter = min(min_perimeter, perimeter)
print(min_perimeter)