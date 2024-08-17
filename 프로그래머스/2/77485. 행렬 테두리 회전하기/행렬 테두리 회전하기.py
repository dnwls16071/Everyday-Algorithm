def solution(rows, columns, queries):
    answer = []
    value = 1
    array = [[0] * columns for _ in range(rows)]
    # 2차원 배열 선언 후 초기화
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = value
            value += 1
    
    # 회전 순서 : 왼쪽 면 → 아래쪽 면 → 오른쪽 면 → 위쪽 면
    # 좌상단 값은 따로 변수에 저장 후 회전 다 돌리면 그 때 넣을 것(그래야 값이 유실되지 않음)
    for query in queries:
        x1, y1, x2, y2 = query
        
        first = array[x1-1][y1-1]
        min_value = first

        # 왼쪽 면
        for i in range(x1, x2):
            array[i-1][y1-1] = array[i][y1-1]
            min_value = min(min_value, array[i][y1-1])
        # 아래쪽 면
        for i in range(y1, y2):
            array[x2-1][i-1] = array[x2-1][i]
            min_value = min(min_value, array[x2-1][i])
        # 오른쪽 면
        for i in range(x2-1, x1-1, -1):
            array[i][y2-1] = array[i-1][y2-1]
            min_value = min(min_value, array[i-1][y2-1])
        # 위쪽 면
        for i in range(y2-1, y1, -1):
            array[x1-1][i] = array[x1-1][i-1]
            min_value = min(min_value, array[x1-1][i-1])
        array[x1-1][y1] = first
        answer.append(min_value)
    return answer