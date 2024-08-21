def solution(brown, yellow):
    answer = []
    area = brown + yellow
    for i in range(1, (area // 2) + 1):
        if area % i == 0:
            answer.append([i, area // i])
    
    for lst in answer:
        if lst[0] >= lst[1] and (lst[0] - 2) * (lst[1] - 2) == yellow:
            return lst