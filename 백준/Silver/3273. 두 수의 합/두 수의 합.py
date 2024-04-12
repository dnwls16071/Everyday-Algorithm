import sys
input = sys.stdin.readline

N = int(input().rstrip())
data = list(map(int, input().split()))
data.sort()
x = int(input())

start = 0
end = N-1

cnt = 0
while start < end:
    result = data[start] + data[end]
    if result == x:
        cnt += 1
        end -= 1
        start += 1
    else:
        if result > x:
            end -= 1
        else:
            start += 1
print(cnt)