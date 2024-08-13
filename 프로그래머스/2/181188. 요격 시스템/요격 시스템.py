def solution(targets):
    targets = sorted(targets, key=lambda x : (x[1], x[0]))
    s = e = 0
    cnt = 0
    for target in targets:
        if e <= target[0]:
            e = target[1]
            cnt += 1
    return cnt