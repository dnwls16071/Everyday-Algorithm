import functools

def xy_compare(n1, n2):
    res1 = n1 + n2
    res2 = n2 + n1
    return (int(res1) > int(res2)) - (int(res1) < int(res2))

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=functools.cmp_to_key(xy_compare), reverse=True)
    answer = str(int(''.join(numbers)))
    return answer