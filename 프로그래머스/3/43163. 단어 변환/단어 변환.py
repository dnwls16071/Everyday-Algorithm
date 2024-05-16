from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    q = deque()
    q.append([begin, 0])
    while q:
        word, v = q.popleft()
        if word == target:
            return v
        else:
            for i in range(len(words)):
                if not visited[i]:
                    if sum(x != y for x, y in zip(word, words[i])) == 1:
                        q.append([words[i], v+1])
                        visited[i] = True
    return 0