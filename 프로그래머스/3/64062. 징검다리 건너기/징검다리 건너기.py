def solution(stones, k):
    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        ct = 0
        for stone in stones:
            if mid >= stone:
                ct += 1
            else:
                ct = 0
            if ct >= k:
                break

        if ct >= k:
            end = mid - 1
        else:
            start = mid + 1            
    return start
