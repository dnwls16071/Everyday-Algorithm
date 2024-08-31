# gems 배열의 크기는 1 이상 100,000 이하
# 2중 for문은 불가 / 투 포인터를 어떻게 배치할 것인지?(양쪽 or 처음부터 같이)
def solution(gems):
    kind = len(set(gems))   # 중복되어 사도 상관은 없지만 모든 종류를 최소 하나씩은 사야하므로

    answer = [0, len(gems) - 1]
    start = end = 0
    lst = dict({gems[0] : 1})
    # 끝에 도달할 때까지 무한 반복문 돌리기
    while end < len(gems):
        if len(lst) < kind:
            end += 1
            if end == len(gems):
                break
            lst[gems[end]] = lst.get(gems[end], 0) + 1
        else:
            # 가장 짧은 구간 갱신
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                answer = [start, end]
            if lst[gems[start]] == 1:
                del lst[gems[start]]
            else:
                lst[gems[start]] -= 1
            start += 1
    return [answer[0] + 1, answer[1] + 1]