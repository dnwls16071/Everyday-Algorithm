def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, val in enumerate(citations):
        if val >= idx + 1:
            h_idx = idx + 1
            answer = h_idx
    return answer