import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0]
sum = 0
for i in range(N):
    sum += array[i]
    prefix_sum.append(sum)

for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])