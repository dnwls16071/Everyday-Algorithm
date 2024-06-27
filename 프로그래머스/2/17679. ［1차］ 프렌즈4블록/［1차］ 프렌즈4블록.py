def solution(m, n, board):
    # 2차원 배열 스타일로 변형
    game = []
    for i in range(m):
        lst = list(board[i])
        game.append(lst)

    answer = 0
    bomb_set = set()
    while True:
        # 2 x 2 사각형 모양의 블록을 구성하는 이모티콘이 같으면 펑
        for i in range(m - 1):
            for j in range(n - 1):
                if game[i][j] == []:
                    continue
                if (game[i][j] == game[i][j+1] == game[i+1][j] == game[i+1][j+1]) and game[i][j] != []:
                    bomb_set.add((i, j))
                    bomb_set.add((i, j+1))
                    bomb_set.add((i+1, j))
                    bomb_set.add((i+1, j+1))

        # 펑 처리되는 블록의 개수 추가
        if bomb_set:
            answer += len(bomb_set)
            # 펑 처리했으면 빈 공간으로 바꾸기
            for y, x in bomb_set:
                game[y][x] = []
            bomb_set = set()
        else:
            break

        # 현재 위치에 블록이 없으면서 현재 위치의 위쪽에 블록이 존재하는 경우
        while True:
            moved = 0
            for i in range(m-1, 0, -1):
                for j in range(n):
                    if game[i][j] == [] and game[i-1][j] != []:
                        game[i][j] = game[i-1][j]
                        game[i-1][j] = []
                        moved += 1
            if moved == 0:
                break
    return answer