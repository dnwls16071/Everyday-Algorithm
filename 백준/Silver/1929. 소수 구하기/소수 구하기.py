import sys
input = sys.stdin.readline

M, N = map(int, input().split())
number = [True] * (N + 1)
number[0] = False
number[1] = False

for i in range(2, int(N**0.5)+1):
    if number[i]:
        for j in range(2*i, N+1, i):
            number[j] = False

for i in range(M, N+1):
    if number[i]:
        print(i)