import math

def solution(n, k):
    n_list = list(range(1, n+1))
    k -= 1  # 0부터 계산하므로
    answer = []
    
    while n_list:
        quo, k = divmod(k, math.factorial(len(n_list) - 1))
        answer.append(n_list.pop(quo))
    return answer