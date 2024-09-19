import sys
input = sys.stdin.readline

N = int(input())

data = []

for _ in range(N):
    name, kor, eng, math = map(str, input().split())
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    data.append([name, kor, eng, math])

data = sorted(data, key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in data:
    print(i[0])