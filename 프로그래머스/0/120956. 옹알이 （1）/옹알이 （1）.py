from itertools import permutations

def solution(babbling):
    answer = 0
    lst = ["aya", "ye", "woo", "ma"]
    words = []
    for i in range(1, 5):
        for j in permutations(lst, i):
            words.append(''.join(j))
            
    for i in babbling:
        if i in words:
            answer += 1
    return answer