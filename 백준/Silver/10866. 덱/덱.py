import sys
input = sys.stdin.readline
from collections import deque

q = deque()
N = int(input())
for _ in range(N):
    commands = list(map(str, input().split()))
    if len(commands) == 2:
        if commands[0] == "push_back":
            q.append(int(commands[1]))
        elif commands[0] == "push_front":
            q.appendleft(int(commands[1]))
    else:
        if commands[0] == "pop_front":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif commands[0] == "pop_back":
            if q:
                print(q.pop())
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