from collections import deque

def solution(board):
    board = [list(map(str, x)) for x in board]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                end = (i, j)

    def BFS(a, b):
        q = deque()
        q.append((a, b, 0))  # 시작점과 이동 횟수를 큐에 저장
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        visited[a][b] = True

        dy = [0, 1, 0, -1]
        dx = [-1, 0, 1, 0]

        while q:
            y, x, move_cnt = q.popleft()
            if (y, x) == end:
                return move_cnt

            for i in range(4):
                ny, nx = y, x
                while True:
                    next_y = ny + dy[i]
                    next_x = nx + dx[i]

                    # 영역 밖을 벗어나면 안 된다.
                    if next_y < 0 or next_y >= len(board) or next_x < 0 or next_x >= len(board[0]):
                        break
                    # 장애물에 부딪히면 끝이다.
                    if board[next_y][next_x] == "D":
                        break

                    ny = next_y
                    nx = next_x

                # 이동한 위치가 아직 방문하지 않은 곳이면 큐에 추가
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, move_cnt + 1))
        return -1

    return BFS(start[0], start[1])