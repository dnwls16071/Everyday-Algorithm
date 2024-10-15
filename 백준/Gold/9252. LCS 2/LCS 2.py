import sys
input = sys.stdin.readline

string1 = list(input().strip())
string2 = list(input().strip())

dp = [[""] * (len(string2) + 1) for _ in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + string1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

if len(dp[-1][-1]) == 0:
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])