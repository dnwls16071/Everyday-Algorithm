def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].add(k + l)
                    dp[i].add(k * l)
                    dp[i].add(k - l)
                    if l != 0 and k != 0:
                        dp[i].add(k // l)
        if number in dp[i]:
            return i
    return -1  