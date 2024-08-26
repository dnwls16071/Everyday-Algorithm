from collections import defaultdict

def solution(clothes):
    info = defaultdict(list)
    for clothe, type in clothes:
        info[type].append(clothe)

    answer = 1
    for key, value in info.items():
        answer *= (len(value) + 1)
    return answer - 1