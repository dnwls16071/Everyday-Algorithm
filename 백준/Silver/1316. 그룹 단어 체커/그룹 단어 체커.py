import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for _ in range(N):
    string = input().strip()
    flag = True
    for idx in range(len(string)-1):
        if string[idx] == string[idx+1]:
            continue
        else:
            if string[idx] in string[idx+1:]:
                flag = False
    
    if flag:
        cnt += 1
print(cnt)