# 시간을 분으로 변환하는 함수
def hour_to_minute_convert(hour, minute):
    return hour * 60 + minute

def solution(plans):    
    result = []
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(":"))
        temp = hour_to_minute_convert(hour, minute)
        plans[i][1] = temp
        plans[i][2] = int(plans[i][2])

    # 시작 시간 순서대로 정렬    
    plans = sorted(plans, key=lambda x : x[1])

    stack = []
    for i in range(len(plans) - 1):
        # gap : 다음 과제 시작 시간과 현재 과제 시작 시간의 차이
        gap = plans[i+1][1] - plans[i][1]
        # [과목명, 과제에 소요되는 시간]
        stack.append([plans[i][0], plans[i][2]])
        
        while stack and gap:
            # 과제에 소요되는 시간이 gap보다 작거나 같으면(즉, 다음 과제 시작 시간 전까지 완료가 가능하다면?)
            if stack[-1][1] <= gap:
                ps, pt = stack.pop()
                gap -= pt
                result.append(ps)
            # 과제에 소요되는 시간이 gap보다 크면(즉, 다음 과제 시작 시간 전까지 완료를 못한다면?)
            else:
                stack[-1][1] -= gap
                gap = 0
    
    result.append(plans[-1][0])
    while stack:
        result.append(stack.pop()[0])
    return result
        