from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1

    for key, val in dic.items():
        answer *= (val + 1)
    return answer - 1