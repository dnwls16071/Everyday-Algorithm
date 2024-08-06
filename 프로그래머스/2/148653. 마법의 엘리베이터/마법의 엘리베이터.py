def solution(storey):
    answer = 0
    while storey != 0:        
        one = storey % 10           # 6
        ten = (storey // 10) % 10   # 1
        
        if one > 5:
            answer += 10 - one      # 20
            storey += (10 - one)
        elif one == 5:
            answer += one
            if ten >= 5:
                storey += 10
        else:
            answer += one
        storey = storey // 10            
    return answer
    