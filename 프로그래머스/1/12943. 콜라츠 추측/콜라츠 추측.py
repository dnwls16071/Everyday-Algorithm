def recur(num, cnt):
    if cnt == 500:
        return -1
    else:
        if num == 1:
            return cnt
        if num % 2 == 0:
            return recur(num // 2, cnt + 1)
        else:
            return recur(num * 3 + 1, cnt + 1)

def solution(num):
    answer = recur(num, 0)
    return answer