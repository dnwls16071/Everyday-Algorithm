def solution(citations):
    answer = 0
    citations.sort()
    c = len(citations)
    for idx, val in enumerate(citations):
        if val >= c - idx:
            return c - idx
    return 0