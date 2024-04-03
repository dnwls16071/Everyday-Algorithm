def solution(N, stages):
    # stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
    cnt = [0] * (N+2)
    users = len(stages)
    for i in stages:
        cnt[i] += 1
    
    result = []
    # (스테이지 번호, 각 스테이지별 인원 수)
    for i in range(1, N+1):
        if users == 0:
            result.append((i, 0))
        else:
            result.append((i, cnt[i] / users))
            users -= cnt[i]
    result = sorted(result, key=lambda x : (-x[1], x[0]))
    result = [i[0] for i in result]
    return result