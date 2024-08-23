def solution(strings, n):
    strings = sorted(list(strings), key=lambda x : (x[n], x))
    return strings