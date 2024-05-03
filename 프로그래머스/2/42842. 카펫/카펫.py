def solution(brown, yellow):
    """
    area : 전체 면적(갈색 타일과 노란색 타일의 합)
    """
    area = brown + yellow
    for i in range(2, brown + 1):
        if area % i == 0:
            a, b = i, area // i
            if (a-2) * (b-2) == yellow:
                return [b, a]