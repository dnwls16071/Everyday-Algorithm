def solution(n):
    answer = [[0] * n for _ in range(n)]
    seq = (n * (n+1)) // 2
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    y = 0; x = 0; direction = 0
    cnt = 1
    
    while cnt <= seq:
        answer[y][x] = cnt
        ny = y + dy[direction]
        nx = x + dx[direction]
        cnt += 1
        
        if (0 <= ny < n) and (0 <= nx < n) and answer[ny][nx] == 0:
            y, x = ny, nx
        else:
            direction = (direction + 1) % 3
            y += dy[direction]
            x += dx[direction]
    
    result = []
    for i in answer:
        for j in i:
            if j == 0:
                break
            else:
                result.append(j)
    return result