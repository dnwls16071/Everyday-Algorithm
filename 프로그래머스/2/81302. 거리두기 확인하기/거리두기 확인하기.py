# Ex. ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"] : 1차원 배열
def check_manhattan(place):
    plist = []
    place = [list(map(str, x)) for x in place]
    for i in range(len(place)):
        for j in range(len(place[i])):
            if place[i][j] == "P":
                plist.append([i, j])
    
    for i in range(len(plist)):
        y1, x1 = plist[i]
        for j in range(i+1, len(plist)):
            y2, x2 = plist[j]
            manhattan_distance = abs(y1 - y2) + abs(x1 - x2)
            if manhattan_distance > 2:
                continue
                
            if manhattan_distance == 1:
                return 0
            elif y1 == y2 and place[y1][(x1 + x2) // 2] != "X":
                return 0
            elif x1 == x2 and place[(y1 + y2) // 2][x1] != "X":
                return 0
            elif x1 != x2 and y1 != y2:
                if place[y1][x2] != "X" or place[y2][x1] != "X":
                    return 0
    return 1
            
def solution(places):
    answer = []
    for place in places:
        answer.append(check_manhattan(place))
    return answer