def solution(N, stages):
    answer = []
    result = []
    state = [0] * (N + 2)   # 라운드별 현황
    for s in stages:
        state[s] += 1
    
    tot = sum(state)
    for idx, s in enumerate(state):
        if tot != 0:
            result.append([idx, s / tot])
        else:
            result.append([idx, 0])
        tot -= s
    result = sorted(result, key=lambda x : (-x[1], x[0]))
    
    for i in result:
        if i[0] == N + 1 or i[0] == 0:
            continue
        answer.append(i[0])
    return answer