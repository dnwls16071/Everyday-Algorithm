from collections import defaultdict

def DFS(graph, path, visited):
    if path:
        o = path[-1]
        if graph[o]:
            path.append(graph[o].pop(0))
        else:
            visited.append(path.pop())
        DFS(graph, path, visited)
    return visited[::-1]

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for c in graph:
        graph[c].sort()
    return DFS(graph, ["ICN"], [])

    