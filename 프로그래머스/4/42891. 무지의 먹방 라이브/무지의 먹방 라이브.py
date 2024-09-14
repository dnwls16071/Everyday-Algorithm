import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for idx, time in enumerate(food_times):
        # 최소힙 구성
        heapq.heappush(q, (time, idx + 1))
    
    sum_times = 0
    previous_times = 0
    length = len(food_times)
    
    while sum_times + (q[0][0] - previous_times) * length <= k:
        now_times = heapq.heappop(q)[0]
        sum_times += (now_times - previous_times) * length
        length -= 1
        previous_times = now_times
    
    result = sorted(q, key=lambda x : x[1])
    return result[(k - sum_times) % length][1]