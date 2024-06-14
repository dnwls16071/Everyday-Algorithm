def conv(num, n):
    dic = {10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    result = []
    if num == 0:
        return ''.join(map(str, [0]))
    else:
        while num != 0:
            if num % n >= 10:
                result.append(dic[num % n])
            else:
                result.append(num % n)
            num //= n
        return ''.join(map(str, result[::-1]))

# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def solution(n, t, m, p):
    result = []
    game_lst = []
    for i in range(m * t):
        # i를 n진법으로 변환
        temp = conv(i, n)
        game_lst.extend(temp)
    for i in range(p-1, m * t, m):
        result.append(game_lst[i])
    return ''.join(map(str, result))