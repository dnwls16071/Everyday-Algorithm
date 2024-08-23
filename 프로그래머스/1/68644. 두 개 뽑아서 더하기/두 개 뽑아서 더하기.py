from itertools import combinations

def solution(numbers):
    result = set()
    for num in combinations(numbers, 2):
        result.add(sum(num))
    result = sorted(result)
    return result

    