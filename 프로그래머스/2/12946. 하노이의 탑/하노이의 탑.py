import sys
sys.setrecursionlimit(10**6)

# 맨 아래 원판을 제외한 (n-1)개의 원판을 1번 기둥에서 2번 기둥으로 옮긴다.
# 맨 아래 원판을 1번 기둥에서 3번 기둥으로 옮긴다.
# 2번 기둥에 있는 (n-1)개의 원판을 3번 기둥으로 옮긴다.
def solution(n):
    answer = []
    
    # n개의 원반을 start(시작 기둥), mid(경유 기둥), end(도착 기둥)
    def hanoi(n, start, mid, end, answer):
        # 1개의 원판은 시작 기둥에서 바로 도착 기둥으로 옮긴다.
        if n == 1:
            return answer.append([start, end])
        # (n-1)개의 원판은 시작 기둥에서 도착 기둥을 경유하여 중간 기둥으로 옮긴다.
        hanoi(n-1, start, end, mid, answer)
        # 1개의 원판은 시작 기둥에서 바로 도착 기둥으로 옮긴다.
        answer.append([start, end])
        # (n-1)개의 원판은 중간 기둥에서 시작 기둥을 경유하여 도착 기둥으로 옮긴다.
        hanoi(n-1, mid, start, end, answer)
    
    hanoi(n, 1, 2, 3, answer)
    return answer