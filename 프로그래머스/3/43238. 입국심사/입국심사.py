# 구하고자 하는 것 : 모든 사람이 심사를 받는데 걸리는 시간
# 테스트케이스 기준 : 6명 인원, 최대 60분 소요

def solution(n, times):
    left = 0
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += (mid // time) # 30분동안 7분 주기로 입국심사를 하면 : 4명 입국심사 가능
            if people > n:
                break
        
        # 입국 심사를 받을 수 잇는 인원이 n명보다 적다면? -> 더 많이 받을 수 있도록 늘려줘야함
        if people < n:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer            