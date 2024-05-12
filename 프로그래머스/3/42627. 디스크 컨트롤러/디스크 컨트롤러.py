from heapq import heappush as push, heappop as pop

def solution(jobs):
    answer, now, idx = 0, 0, 0
    start = -1
    heap = []
    
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                push(heap, job[::-1])
                
        if len(heap) > 0:
            current = pop(heap)
            start = now
            idx += 1
            now += current[0] 
            answer += (now - current[1])            
        else:
            now += 1
    return answer // len(jobs)