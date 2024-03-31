def solution(s):
    answer = len(s)
    for i in range(1, (len(s)//2)+1):
        compressed = ""
        prev = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            curr = s[j:j+i]
            if prev == curr:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += prev
                else:
                    compressed += str(cnt) + prev
                prev = curr
                cnt = 1
        if cnt != 1:
            compressed += str(cnt) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer