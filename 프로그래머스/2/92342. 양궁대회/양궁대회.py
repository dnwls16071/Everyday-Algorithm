from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1    # 최대 점수 차이 갱신
    
    # [0 ~ 10점 중복 조합 계산]
    # k점을 어피치가 a발, 라이언이 b발 맞혔을 경우 더 많은 화살을 k점에 맞힌 선수가 k점을 가져간다.
    # a = b일 경우 어피치가 k점을 가져간다.
    # a = b = 0일 경우 아무도 안 가져간다
    # info의 i번째 원소 : (10 - i)점, ex) 0번째 : 10점
    for score in combinations_with_replacement(range(11), n):
        case = [0] * 11
        for s in score:
            case[10 - s] += 1

        apeach = 0
        lion = 0
        for idx in range(11):
            if info[idx] == case[idx] == 0:
                continue
            
            if info[idx] >= case[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx
        
        if lion > apeach:
            temp = lion - apeach
            if temp > max_gap:
                answer = case
                max_gap = temp

    return answer