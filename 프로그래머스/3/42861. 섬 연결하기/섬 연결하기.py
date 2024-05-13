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

def solution(n, costs):
    answer = 0
    ct = 0  # 간선의 갯수
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x : x[2])
    for cost in costs:
        a, b, c = cost
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += c
            ct += 1
        if ct == n-1:
            break
    return answer