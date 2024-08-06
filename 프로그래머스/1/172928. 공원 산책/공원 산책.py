def solution(park, routes):
    dic = {"N" : [-1, 0], "S" : [1, 0], "E" : [0, 1], "W" : [0, -1]}
    # 시작점
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                y = i
                x = j
                break
    
    for route in routes:
        route = route.split(" ")
        sy, sx = y, x
        
        for _ in range(int(route[1])):
            ny = y + dic[route[0]][0]
            nx = x + dic[route[0]][1]
            print(ny, nx)
            # 지도 밖을 벗어난 경우
            if nx < 0 or nx >= len(park[0]) or ny < 0 or ny >= len(park):
                y, x = sy, sx
                break
            
            # 장애물이 있는 경우
            if park[ny][nx] == "X":
                y, x = sy, sx
                break
            y, x = ny, nx
    return [y, x]