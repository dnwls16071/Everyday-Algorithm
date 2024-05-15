from collections import defaultdict

def solution(tickets):
    hist = defaultdict(list)
    for ticket in tickets:
        a, b =  ticket
        hist[a].append(b)
    
    for h in hist.keys():
        hist[h].sort()

    path = []
    def DFS(start):
        while hist[start]:
            DFS(hist[start].pop(0))
        path.append(start)
    DFS("ICN")
    return path[::-1]