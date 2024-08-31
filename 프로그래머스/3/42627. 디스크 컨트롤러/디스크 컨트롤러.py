import heapq

def solution(jobs):
    start = -1  # 시작 시간
    time = 0    # 걸린 시간
    now = 0     # 현재 시점
    cnt = 0     # 작업 처리 개수
    pq = []     # 우선순위 큐

    # [작업 소요시간, 작업 요청 시점]
    while cnt < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(pq, job[::-1])
        
        # 우선순위 큐에 작업이 들어오면?
        if len(pq) > 0:
            cur = heapq.heappop(pq)
            start = now
            now += cur[0]
            time += (now - cur[1])
            cnt += 1
        else:
            now += 1
    return time // len(jobs)