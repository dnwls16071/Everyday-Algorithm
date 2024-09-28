from collections import deque
import sys

li = deque([])
N = int(input())
for _ in range(N):
    command = list(map(str, sys.stdin.readline().strip().split()))
    if len(command) == 2:
        if command[0] == "push":
            li.append(int(command[1]))
    else:
        if command[0] == "pop":
            if len(li) == 0:
                print(-1)
            else:
                temp = li.popleft()
                print(temp)
        elif command[0] == "size":
            print(len(li))
        elif command[0] == "empty":
            if len(li) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if len(li) == 0:
                print(-1)
            else:
                print(li[0])
        elif command[0] == "back":
            if len(li) == 0:
                print(-1)
            else:
                print(li[-1])