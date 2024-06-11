import sys
input = sys.stdin.readline

String = list(input().strip())
stack = []

for i in range(len(String)):
    if len(stack) >= 4:
        if ''.join(map(str, stack[-4:])) == "PPAP":
            for _ in range(4):
                stack.pop()
            stack.append("P")
    stack.append(String[i])

result = ''.join(map(str, stack))
if result == "PPAP" or stack == ["P"]:
    print("PPAP")
else:
    print("NP")