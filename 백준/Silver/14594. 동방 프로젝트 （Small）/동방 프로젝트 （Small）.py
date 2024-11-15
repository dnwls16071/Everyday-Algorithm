import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
room = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x, y):
        room[i] = 1

answer = room[1:].count(0)
print(answer)