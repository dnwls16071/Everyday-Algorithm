def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()    # 바위 정렬 O(N log N)
    answer = 0
    left = 0
    right = distance
    while left <= right:
        prev = 0       
        removed = 0
        mid = (left + right) // 2

        for rock in rocks:
            if rock - prev < mid: 
                removed += 1
            else:                  
                prev = rock
            if removed > n:
                break

        if removed > n: # 제거한 바위의 개수가 n개보다 많다면?
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer