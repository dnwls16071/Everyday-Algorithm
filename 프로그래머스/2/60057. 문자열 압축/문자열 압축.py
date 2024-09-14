def solution(s):
    answer = len(s)
    result = []
    # 절반 범위까지만 탐색(압축 범위)
    for idx in range(1, (len(s) // 2) + 1):    
        temp = []       # 중간 압축 결과 저장
        prev = s[:idx]
        cnt = 1         # 연이어 등장하는 문자의 개수
        for j in range(idx, len(s) + idx, idx):
            curr = s[j:j+idx]
            
            if prev == curr:
                cnt += 1
            else:
                if cnt > 1:
                    temp.append(str(cnt) + prev)
                else:
                    temp.append(prev)
                cnt = 1
                prev = curr
        result.append(''.join(map(str, temp)))
    
    for s in result:
        answer = min(answer, len(s))
    return answer