import sys
input = sys.stdin.readline

N, C = map(int, input().split())
data = [int(input()) for _ in range(N)]
data.sort()
answer = 0

def binary_search(data):
    global answer
    start = 1                       # 한 집에 하나만 설치할 수 있으므로 공유기 사이의 최소 거리는 1부터 시작
    end = data[-1] - data[0]        # 공유기 사이 최대 거리(맨 앞 집 - 맨 뒤 집)
    while start <= end:
        mid = (start + end) // 2    # 공유기 사이 거리
        pos = data[0]               # 첫 집에 설치한다고 가정
        cnt = 1                     # 공유기 개수 카운팅
        
        for i in range(1, N):
            if data[i] >= pos + mid:
                cnt += 1
                pos = data[i]
        
        # 공유기의 개수가 C개 이상이라면?
        if cnt >= C:
            start = mid + 1
            answer = mid
        # 공유기의 개수가 C개 미만이라면?
        else:
            end = mid - 1
            
binary_search(data)
print(answer)