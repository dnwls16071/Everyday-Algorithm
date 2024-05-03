def solution(brown, yellow):
    area = brown + yellow
    for i in range(1, brown + 1):
        if area % i == 0:
            a, b = i, area // i
            if (a-2) * (b-2) == yellow:
                return [b, a]