from itertools import combinations

def solution(relation):
    cnt = 0
    # 컬럼 인덱스 조합
    col_comb = []
    for i in range(1, len(relation[0])+1):
        col_comb.extend(combinations(range(1, len(relation[0])+1), i))

    # 유일성 : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
    unique_lst = []
    for col in col_comb:
        temp = [tuple(record[key-1] for key in col) for record in relation]
        if len(set(temp)) == len(relation):
            unique_lst.append(col)
    
    # 최소성 : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
    # 교집합을 구하는 연산 → (1, 2)와 (1, 2, 3)을 교집합 연산을 취하게 되면 (1, 2)가 나오게 되는데 (1, 2, 3) 입장에서 보면 유일성이 깨지는 것이기 때문에 (1, 2, 3)은 제거해주는 것
    answer = set(unique_lst)
    for u in range(len(unique_lst)):
        for j in range(u+1, len(unique_lst)):
            if len(unique_lst[u]) == len(set(unique_lst[u]) & set(unique_lst[j])):
                answer.discard(unique_lst[j])
    return len(answer)