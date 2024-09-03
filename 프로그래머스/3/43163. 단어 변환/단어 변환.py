from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    visited = [False] * len(words)
    while q:
        b, cnt = q.popleft()
        if b == target:
            return cnt
        for idx in range(len(words)):
            temp = 0
            if not visited[idx]:
                for x, y in zip(b, words[idx]):
                    if x != y:
                        temp += 1
                if temp == 1:
                    visited[idx] = True
                    q.append([words[idx], cnt + 1])
    return 0