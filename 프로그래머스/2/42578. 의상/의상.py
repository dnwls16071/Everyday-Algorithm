### 아무것도 입지 않은 경우만 제외

from collections import Counter

def solution(clothes):
    answer = 1
    dictionary = Counter(i[1] for i in clothes)
    for i in dictionary.values():
        answer *= (i+1)
    answer -= 1
    return answer