import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
result = []

N = int(input())
min_heap = []; max_heap = []
for _ in range(N):
    P, L = map(int, input().split())
    # 단일 값이 아닌 값을 힙에 넣으면 첫 번째 원소를 기준으로 힙을 구성한다.
    # 최소힙 : 문제 번호가 작은 순서대로
    # 최대힙 : 문제 번호가 큰 순서대로
    heapq.heappush(min_heap, [L, P])
    heapq.heappush(max_heap, [-L, -P])    

M = int(input())
solved = defaultdict(int)   # 같은 문제지만 난이도가 달리 추가될 수 있으므로 bool → int
for _ in range(M):
    commands = list(input().split())
    if commands[0] == "recommend":
        # 문제 리스트에서 가장 어려운 문제 번호를 출력
        if commands[1] == "1":
            # 풀지 않은 문제라면?
            while solved[abs(max_heap[0][1])] != 0:
                solved[abs(max_heap[0][1])] -= 1
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        elif commands[1] == "-1":
            # 풀지 않은 문제라면?
            while solved[min_heap[0][1]] != 0:
                solved[min_heap[0][1]] -= 1
                heapq.heappop(min_heap)
            print(min_heap[0][1])
    elif commands[0] == "add":
        heapq.heappush(min_heap, [int(commands[2]), int(commands[1])])
        heapq.heappush(max_heap, [-int(commands[2]), -int(commands[1])])
    elif commands[0] == "solved":
        solved[int(commands[1])] += 1