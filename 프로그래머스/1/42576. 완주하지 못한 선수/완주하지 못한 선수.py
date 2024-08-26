from collections import Counter

def solution(participant, completion):
    counter = Counter(participant)
    for comp in completion:
        if counter[comp] > 0:
            counter[comp] -= 1
        
    for key, value in counter.items():
        if value != 0:
            return key