import sys
input = sys.stdin.readline

M, N = map(int, input().split())
array = [True] * (N+1)
array[1] = False

for i in range(2, int(N**0.5)+1):
    if array[i]:
        for j in range(i*i, N+1, i):
            array[j] = False

for i in range(M, N+1):
    if array[i]:
        print(i)