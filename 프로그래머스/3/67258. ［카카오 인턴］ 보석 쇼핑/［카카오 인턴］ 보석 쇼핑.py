from collections import defaultdict
from heapq import heappush as push, heappop as pop

def solution(gems):
    kind = len(set(gems))   # 중복을 제거하여 나올 수 있는 모든 보석의 종류의 수 
    start = 0               # 시작 지점
    dic = defaultdict(int)  # 보석의 소유 현황을 나타내는 딕셔너리
    heap = []               

    for end, gem in enumerate(gems):
        dic[gem] += 1       # 해당 보석을 소유하므로 갯수 증가
        
        # 소유한 보석의 종류의 수가 주어진 보석 종류의 수와 같을 때까지
        while len(dic) == kind:
            # 조건을 만족할 때마다 해당되는 시점을 힙에 저장
            push(heap, [end - start, start + 1, end + 1])
            # 앞에서부터 하나씩 빼보기
            dic[gems[start]] -= 1
            # 해당 원소를 보유하고 있지 않다면 제거
            if not dic[gems[start]]:
                del dic[gems[start]]
            start += 1
    answer = [heap[0][1], heap[0][2]]
    return answer