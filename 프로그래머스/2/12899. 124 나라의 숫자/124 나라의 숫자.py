# 단순 규칙성 파악 문제

def solution(n):
    answer = []
    while n > 0:
        n -= 1
        q, x = divmod(n, 3)
        if x == 0:
            answer.append(1)
        elif x == 1:
            answer.append(2)
        elif x == 2:
            answer.append(4)
        n = q
    return ''.join(map(str, answer[::-1]))