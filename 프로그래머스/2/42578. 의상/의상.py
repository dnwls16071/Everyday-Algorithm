from collections import defaultdict

def solution(clothes):
    """
    전체 입을 수 있는 의상의 조합 수에서 아무것도 안 입은 경우에 해당하는 값인 1을 뺀다.
    """
    answer = 1
    dic = defaultdict(int)
    for c in clothes:
        dic[c[1]] += 1

    for key, val in dic.items():
        answer *= (val + 1)
    return answer - 1