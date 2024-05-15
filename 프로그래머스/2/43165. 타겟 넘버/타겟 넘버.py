from collections import deque

def solution(numbers, target):
    n = len(numbers)
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1*numbers[0], 0])
    answer = 0
    while q:
        v, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([v + numbers[idx], idx])
            q.append([v - numbers[idx], idx])
        else:
            if v == target:
                answer += 1
    return answer