from heapq import heappush as push, heappop as pop

def solution(jobs):
    answer = 0
    now = 0
    idx = 0
    start = -1
    heap = []
    
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                push(heap, job[::-1])      
        
        if len(heap) > 0:
            cur = pop(heap)
            start = now
            idx += 1
            now += cur[0]
            answer += (now - cur[1])
        else:
            now += 1
    return answer // len(jobs)