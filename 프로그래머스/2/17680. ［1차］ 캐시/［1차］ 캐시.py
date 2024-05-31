from collections import deque

def solution(cacheSize, cities):    
    """
    데크(deque)의 최대 크기 지정
    → cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
    """
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        """
        TestCase#5 - "NewYork", "newyork"
        → 동일하게 처리해야하므로 소문자로 처리를 하든 대문자로 처리를 하든 하나로 통일해야함
        """
        city = city.lower()
        """
        LRU(Least Recently Used)
        : 가장 오랫동안 사용되지 않은 페이지를 제거
        : 이 때, cache miss인 경우 바로 넣어주기만 하면 끝
        : 반면 cache hit인 경우 기존에 들어있는 도시를 삭제 후 마지막에 도시를 반영
        """
        # cache miss(캐시에 존재하지 않는 경우)
        if city not in cache:
            time += 5
        # cache hit(캐시에 존재하는 경우)
        else:
            cache.remove(city)
            time += 1
        cache.append(city)
    return time
            