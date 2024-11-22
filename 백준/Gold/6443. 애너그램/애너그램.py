import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

def recur(idx, comb):
    if idx == len(word):
        print(''.join(map(str, comb)))
        return

    prev = None
    for i in range(len(word)):
        if not visited[i]:
            curr = word[i]
            if prev != curr:
                visited[i] = True
                comb.append(word[i])
                recur(idx + 1, comb)
                comb.pop()
                visited[i] = False
                prev = curr

for _ in range(N):
    word = sorted(input().strip())
    visited = [False] * (len(word) + 1)
    recur(0, [])