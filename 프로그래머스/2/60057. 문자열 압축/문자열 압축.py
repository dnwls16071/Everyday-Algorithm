def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        prev = s[:i]
        cnt = 1
        temp = 0
        for j in range(i, len(s)+i, i):
            curr = s[j:j+i]
            if prev == curr:
                cnt += 1
            else:
                if cnt != 1:
                    temp += len(str(cnt)) + len(prev)
                else:
                    temp += len(prev)
                cnt = 1
                prev = curr
        answer = min(answer, temp)
        temp = 0
    return answer