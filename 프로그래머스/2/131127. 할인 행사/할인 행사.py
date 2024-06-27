from collections import Counter, defaultdict

def solution(want, number, discount):
    answer = 0
    dic = defaultdict(int)
    for w, n in zip(want, number):
        dic[w] = n    
    
    for i in range(len(discount)):
        c = Counter(discount[i:i+10])
        if c == dic:
            answer += 1
    return answer