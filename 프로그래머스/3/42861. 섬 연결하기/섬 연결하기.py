# 주어진 노드가 집합 안에 포함이 되는지를 확인
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 합집합 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    # 작은 쪽에 맞추기
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0  # 비용
    parent = [i for i in range(n+1)]
    costs = sorted(costs, key=lambda x : x[2])  # 비용 순으로 정렬
    for cost in costs:
        # 부모가 일치하지 않으면 합집합 연산을 수행하도록
        if find(parent, cost[0]) != find(parent, cost[1]):
            union(parent, cost[0], cost[1])
            answer += cost[2]
    return answer