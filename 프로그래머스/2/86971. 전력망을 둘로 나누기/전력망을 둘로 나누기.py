import copy

def solution(n, wires):
    res = []
    parent = [i for i in range(n+1)]
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    for i in range(len(wires)):         # 끊을 간선
        parent_cp = parent[:]
        for j in range(len(wires)):     
            if i == j:                  # 연결 안하기
                continue                
            a, b = wires[j]             # 안 끊고 Union-Find
            union(parent_cp, a, b)
        for a, b in wires:
            parent_cp[a] = find(parent_cp, a)
            parent_cp[b] = find(parent_cp, b)
        ra = parent_cp.count(parent_cp[wires[i][0]])
        rb = parent_cp.count(parent_cp[wires[i][1]])
        res.append(abs(ra - rb))
    return min(res)