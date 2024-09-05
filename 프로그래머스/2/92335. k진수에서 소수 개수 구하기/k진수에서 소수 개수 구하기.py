def change(n, k):
    ret = []
    while n > 0:
        ret.append(str(n % k))
        n //= k
    return ''.join(ret[::-1])

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    ret = change(n, k)
    ret = ret.split('0')
    answer = 0
    for r in ret:
        if not r:
            continue
        if is_prime(int(r)):
            answer += 1
    return answer
    