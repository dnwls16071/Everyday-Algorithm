import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    commands = list(map(str, input().split()))
    if len(commands) == 2:
        stack.append(int(commands[1]))
    else:
        if commands[0] == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif commands[0] == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif commands[0] == "size":
            print(len(stack))
        elif commands[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)