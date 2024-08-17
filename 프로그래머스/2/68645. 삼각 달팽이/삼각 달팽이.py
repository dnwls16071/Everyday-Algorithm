def solution(n):
    answer = []
    array = [[0] * n for _ in range(n)]
    val = n * (n + 1) // 2
    
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    y = 0; x = 0; direction = 0
    for i in range(1, val+1):
        array[y][x] = i
        ny = y + dy[direction]
        nx = x + dx[direction]
        # 영역 범위 안이면서 아직 값을 채워넣지 않은 경우
        if (0 <= ny < n and 0 <= nx < n and not array[ny][nx]):
            y, x = ny, nx
        # if문 조건 외 → 방향 전환(↓ → ↖)
        else:
            direction = (direction + 1) % 3
            # 영역 가장자리 충돌 시 방향을 회전함과 동시에 위치를 한 칸 이동시켜줌
            y += dy[direction]     
            x += dx[direction]
    
    for i in array:
        for j in i:
            if j:
                answer.append(j)
    return answer