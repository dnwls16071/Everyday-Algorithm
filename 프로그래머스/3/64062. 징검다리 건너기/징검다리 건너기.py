def moving_check(n, stones, k):
    skip = 0    # 최대 건너뛸 수 있는 칸의 수가 k보다 크면 건너뛸 수 없어 결국 종료
    for stone in stones:
        if stone < n:
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0
    return True

def solution(stones, k):
    left = 0
    right = 200000001
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if moving_check(mid, stones, k):
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1
    return answer