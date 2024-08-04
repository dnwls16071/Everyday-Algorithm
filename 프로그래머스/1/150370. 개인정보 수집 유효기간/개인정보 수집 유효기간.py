from collections import defaultdict

# 모든 달은 28일까지 있다고 가정합니다.
def day_to_num(today):
    lst = today.split(".")
    return int(lst[0]) * 28 * 12 + int(lst[1]) * 28 + int(lst[2])

def solution(today, terms, privacies):
    answer = []
    dic = defaultdict(int)
    today = day_to_num(today)
    # 1. terms 딕셔너리로 관리
    for term in terms:
        term = term.split(" ")
        dic[term[0]] = int(term[1])
    
    # 2. 개인정보 보호 기간 만족 여부 확인하기
    for idx, privacy in enumerate(privacies):
        privacy = privacy.split(" ")
        # privacy_day : 유효기간
        privacy_day = day_to_num(privacy[0]) + dic[privacy[1]] * 28
        if (today >= privacy_day):
            answer.append(idx + 1)
    return answer