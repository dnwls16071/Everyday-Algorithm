def solution(N, number):
    dp = [set() for i in range(9)]  # N을 i번 사용해서 얻을 수 있는 숫자들의 모임 
    for i in range(1, 9):           
        dp[i].add(int(str(N) * i))  # N을 i번 사용(기본값)
        for j in range(1, i):
            for k in dp[j]:
                for t in dp[i-j]:
                    dp[i].add(k + t)
                    dp[i].add(k - t)
                    dp[i].add(k * t)
                    if t != 0 and k != 0:
                        dp[i].add(k // t)
        if number in dp[i]:
            return i
    return -1