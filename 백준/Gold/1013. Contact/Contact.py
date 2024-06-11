import sys, re
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    p = re.compile('(100+1+|01)+')
    a = input().strip()
    if p.fullmatch(a):
        print("YES")
    else:
        print("NO")