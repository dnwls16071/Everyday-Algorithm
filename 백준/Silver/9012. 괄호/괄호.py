import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = input().strip()
    stack = []
    for s in string:
        if s == "(":
            stack.append("(")
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
    if stack:
        print("NO")
    else:
        print("YES")