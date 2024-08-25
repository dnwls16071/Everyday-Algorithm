from collections import defaultdict
from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    # 지원자 정보를 기반으로 조합을 산출
    # 키에는 점수를 제외한 지원자 정보, 값에는 지원자 점수 리스트(선형 탐색X)
    data = defaultdict(list)    
    
    for i in info:  
        i = i.split(" ")                              # java backend junior pizza
        score = int(i.pop())                          # 150
        data["".join(i)].append(score)                # javabackendjuniorpizza
        for j in range(4):
            case = list(combinations(i, j))           # 지원자 정보 조합
            for k in case:
                data["".join(k)].append(score)
    
    for key, value in data.items():
        data[key].sort()
    
    for q in query:
        q = q.split(" ")
        score = int(q.pop())
        key = "".join(q)
        key = key.replace("and", "").replace(" ", "").replace("-", "")
        answer.append(len(data[key]) - bisect_left(data[key], score))
    return answer