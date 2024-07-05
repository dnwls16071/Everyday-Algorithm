from collections import Counter
from itertools import combinations

# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합

def solution(orders, course):
    # course : [2, 3, 4] → 코스 요리를 구성하는 단품메뉴들의 개수
    # orders : ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] → 주문한 단품메뉴들 
    max_num = max([len(order) for order in orders])
    answer = []
    for c in course:
        counter = Counter()
        for order in orders:
            # 하나의 코스 요리를 구성하는데 필요한 단품메뉴의 개수(Ex. 2)
            # 손님이 주문한 단품메뉴들의 수보다 많은 경우(Ex. 3)
            if c > max_num:
                continue
            menu_comb = list(combinations(sorted(order), c))
            counter += Counter(menu_comb)
        mp = max(counter.values(), default=0)  # empty sequence에서 max로 최댓값을 찾지 못하는 오류 방지
        for key, value in counter.items():
            # 최소 2명 이상의 손님으로부터 주문되어야 하면서
            # 하나의 코스 요리를 구성하는데 필요한 단품메뉴의 개수가 충족되는지를 체크
            if value == mp and value >= 2:
                answer.append("".join(map(str, key)))
    # 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return
    answer.sort()
    return answer