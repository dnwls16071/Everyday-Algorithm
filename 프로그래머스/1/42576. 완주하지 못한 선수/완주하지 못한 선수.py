from collections import Counter

def solution(participant, completion):
    non_completion = []
    dic = Counter(participant)
    for i in completion:
        if dic[i]:
            dic[i] -= 1
        else:
            non_completion.append(dic[i])
    
    for key, value in dic.items():
        if value != 0:
            non_completion.append(key)
    return "".join(map(str, non_completion))