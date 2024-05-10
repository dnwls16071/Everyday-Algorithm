def solution(money):
    """
    [1]. 첫 번째 집을 털고 세 번째 집을 턴다.
    [2]. 두 번째 집을 털고 그 다음 집은 털지 않는다.
    """
    dp1 = [0] * len(money) 
    dp2 = [0] * len(money)
    # 첫 번째 집 털고 세 번째 집을 턴다.
    dp1[0] = dp1[1] = money[0]
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
    
    # 두 번째 집을 턴다.
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i]) 
    return max(max(dp1), max(dp2))