def solution(line):
    answer = []
    # 격자판 최대 영역 변수
    INF = int(1e15)
    MAX_X = -INF; MAX_Y = -INF
    MIN_X = INF; MIN_Y = INF
    dots = []

    for i in range(len(line)):
        a, b, c = line[i]
        for j in range(i + 1, len(line)):
            d, e, f = line[j]
            # 두 직선의 기울기가 같아 평행하다면 교점은 안 생김
            if a * e == b * d:
                continue
            # 두 직선의 교점 좌표(x, y)
            x = (c * e - b * f) / (b * d - a * e)
            y = (a * f - c * d) / (b * d - a * e)
            # 정수값만
            if int(x) == x and int(y) == y:
                MIN_X = min(MIN_X, int(x))
                MAX_X = max(MAX_X, int(x))
                MIN_Y = min(MIN_Y, int(y))
                MAX_Y = max(MAX_Y, int(y))               
                dots.append([int(x), int(y)])

    width = abs(MAX_X - MIN_X + 1)
    height = abs(MAX_Y - MIN_Y + 1)
    array = [["."] * width for _ in range(height)]  
    
    for x, y in dots:
        if MIN_X < 0:
            nx = x + abs(MIN_X)
        else:
            nx = x - MIN_X
        
        if MIN_Y < 0:
            ny = y + abs(MIN_Y)
        else:
            ny = y - MIN_Y
        array[ny][nx] = "*"
    
    for i in array:
        answer.append("".join(i))
    return answer[::-1]