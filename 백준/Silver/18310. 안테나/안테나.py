import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

if N % 2 == 0:
    f1 = data[(N // 2) - 1]
    f2 = data[N // 2]
    print(min(f1, f2))
else:
    print(data[N // 2])