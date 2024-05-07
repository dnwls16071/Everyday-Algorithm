from collections import defaultdict

def solution(participant, completion):
    maraton = defaultdict(int)
    for p in participant:
        maraton[p] += 1
    
    for c in completion:
        maraton[c] -= 1
    
    for key, val in maraton.items():
        if val != 0:
            return key