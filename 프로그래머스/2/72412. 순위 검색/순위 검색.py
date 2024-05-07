from itertools import combinations
from bisect import bisect_left, bisect_right
from collections import defaultdict

def solution(info, query):
    result = []
    """
    개발언어 : cpp, java, python
    직군 : backend, frontend
    경력 : junior, senior
    소울푸드 : chicken, pizza
    총 조합의 수 : 3 x 2 x 2 x 2 = 24
    """
    hash_info = defaultdict(list)
    for i in info:
        c = i.split(" ")[:]
        score = c.pop()
        for r in range(5):
            combs = combinations(range(4), r)
            for comb in combs:
                key = c[:]
                for idx in comb:
                    key[idx] = "-"
                hash_info["".join(key)].append(int(score))

    for key in hash_info.keys():
        hash_info[key].sort()
                
    for q in query:
        c = q.replace(" and", "").split(" ")
        score = int(c.pop())
        key = "".join(c)
        if key not in hash_info:
            result.append(0)
        else:
            right_idx = len(hash_info[key])
            left_idx = bisect_left(hash_info[key], score)
            result.append(right_idx - left_idx)
    return result
            