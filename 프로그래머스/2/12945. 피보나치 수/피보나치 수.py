import sys
sys.setrecursionlimit(10**6)

def fibo(n, dp):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    if dp[n] == 0:
        dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n] % 1234567
            
def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = dp[2] = 1
    return fibo(n, dp)