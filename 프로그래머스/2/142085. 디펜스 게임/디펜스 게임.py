import heapq

def solution(n, k, enemy):
    heap = []
    answer = 0
    num = 0
    for e in enemy:
        heapq.heappush(heap, -e)
        num += e
        if num > n:
            if k == 0:
                break
            k -= 1
            num += heapq.heappop(heap)
        answer += 1
    return answer