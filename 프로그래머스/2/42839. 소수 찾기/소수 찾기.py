from itertools import permutations

def check(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    cnt = 0
    lst = list(map(str, numbers))

    res = set()
    for i in range(1, len(lst) + 1):
        for perm in permutations(lst, i):
            num = int("".join(map(str, perm)))
            if check(num) and num not in res:
                res.add(num)
    return len(res)