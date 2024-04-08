from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    prefix = [[] for _ in range(10001)]
    suffix = [[] for _ in range(10001)]
    for word in words:
        prefix[len(word)].append(word)
        suffix[len(word)].append(word[::-1])        
    for i in range(10001):
        prefix[i].sort()
        suffix[i].sort()
    for q in queries:
        # 접미사로 ?이 등장하는 경우
        if q[0] != "?":
            left_idx = bisect_left(prefix[len(q)], q.replace("?", "a"))
            right_idx = bisect_right(prefix[len(q)], q.replace("?", "z"))
        # 접두사로 ?이 등장하는 경우
        else:
            left_idx = bisect_left(suffix[len(q)], q[::-1].replace("?", "a"))
            right_idx = bisect_right(suffix[len(q)], q[::-1].replace("?", "z"))
        answer.append(right_idx - left_idx)
    return answer