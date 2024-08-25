from itertools import combinations
from collections import defaultdict

def binary_search(score, key):
    left = 0
    right = len(score)
    while left < right:
        mid = (left + right) // 2
        if score[mid] >= key:
            right = mid
        else:
            left = mid + 1
    return len(score) - left
        
def solution(info, query):
    answer = []
    data = defaultdict(list)
    for i in info:
        i = i.split(" ")
        score = int(i.pop())
        for j in range(5):
            for comb in combinations(i, j):
                key = "".join(comb)
                data[key].append(score)
    
    for key, value in data.items():
        data[key].sort()    # O(N log N)
    
    for q in query:
        q = q.split(" ")
        score = int(q.pop())
        key = "".join(q)
        key = key.replace("and", "").replace("-", "").replace(" ", "")
        answer.append(binary_search(data[key], score))
    return answer