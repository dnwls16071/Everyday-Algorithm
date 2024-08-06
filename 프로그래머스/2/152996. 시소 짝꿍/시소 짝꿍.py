from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights) 
    
    for key, value in counter.items():
        if value >= 2:
            answer += (value * (value - 1)) // 2
        if key * (2/4) in counter:
            answer += counter[key] * counter[key * (2/4)]
        if key * (2/3) in counter:
            answer += counter[key] * counter[key * (2/3)]
        if key * (3/4) in counter:
            answer += counter[key] * counter[key * (3/4)]
    return answer
        