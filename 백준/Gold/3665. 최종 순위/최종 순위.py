import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    indegree = [0] * (n + 1)                            # 진입 차수 배열
    graph = [[False] * (n + 1) for _ in range(n + 1)]   # 인접 행렬
    rank = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[i]][rank[j]] = True  # 연결 정보 True
            indegree[rank[j]] += 1          # i가 j보다 순위가 높은 것이므로
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())    # 순위가 바뀐 팀
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1    # b팀의 순위가 높아지게 되면 a팀 입장에서 보았을 때 앞쪽에 한 팀이 자리잡게 되므로 진입 차수 배열을 +1
            indegree[b] -= 1    # a팀의 순위가 낮아지게 되면 b팀 입장에서 보았을 때 뒤쪽에 한 팀이 자리잡게 되므로 진입 차수 배열을 -1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1
    
    result = []
    q = deque()
    # 진입 차수 값이 0이면 먼저 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 인원 수만큼 돌렸는데 그 전에 진입 차수가 비어있게 된다면? → 사이클이 존재함
    # 또한 큐의 원소가 두 개 이상이라면? → 위상 정렬의 결과가 여러 가지가 나올 수 있음
    cycle = False
    flag = False
    
    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
    
        if len(q) >= 2:
            flag = True
            break

        v = q.popleft()
        result.append(v)
        for j in range(1, n+1):
            if graph[v][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:   # 사이클이 발생한다면?
        print("IMPOSSIBLE")
    elif flag:  # 확실한 순위를 찾을 수 없다면?
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()