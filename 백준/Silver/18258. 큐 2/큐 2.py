import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    commands = list(map(str, input().split()))
    if len(commands) == 2:
        q.append(int(commands[1]))
    else:
        if commands[0] == "pop":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif commands[0] == "size":
            print(len(q))
        elif commands[0] == "empty":
            if q:
                print(0)
            else:
                print(1)
        elif commands[0] == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif commands[0] == "back":
            if q:
                print(q[-1])
            else:
                print(-1)