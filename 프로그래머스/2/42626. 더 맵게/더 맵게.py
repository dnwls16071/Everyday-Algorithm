import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        try:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
            answer += 1
        except IndexError:
            return -1