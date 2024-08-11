def solution(k, ranges):
    array = []  # 콜라츠 수열 저장 배열
    area = []   # 정적분 결과 저장 배열
    while k != 1:
        cn = k
        if k % 2 != 0:
            array.append(k * 3 + 1)
            k = k * 3 + 1
        else:
            array.append(k // 2)
            k //= 2
        area.append((cn + k) / 2)
    
    prefix_sum = [0] * (len(area) + 1)
    temp = 0
    for i in range(len(area)):
        temp += area[i]
        prefix_sum[i + 1] = temp
        
    answer = []
    for x1, x2 in ranges:
        if x1 >= x2:
            a = x1
            b = len(area) + x2
            if a > b:
                answer.append(-1.0)
            else:
                answer.append("{:.1f}".format(prefix_sum[b] - prefix_sum[a]))
        else:
            answer.append(-1.0)
    return answer