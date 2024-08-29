def solution(money):
    # 원형으로 되어있기 때문에 만약 첫 번째 집부터 턴다고 가정한다면
    # 마지막 집은 털 수 없다.
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
        
    # 원형으로 되어있기 때문에 만약 두 번째 집부터 턴다고 가정한다면
    # 마지막 집을 털 수 있다.
    dp2 = [0] * len(money)
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
    
    return max(max(dp1), max(dp2))