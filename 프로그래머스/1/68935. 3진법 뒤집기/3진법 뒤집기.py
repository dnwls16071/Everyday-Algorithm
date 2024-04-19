def solution(n):
    res = convert(n)
    Sum = 0
    for i in range(len(res)):
        Sum += res[i] * (3 ** i)
    return Sum


def convert(n):
    res = []
    while n != 0:
        res.append(n % 3)
        n //= 3
    return res[::-1]