from itertools import combinations
import sys
input = sys.stdin.readline

String = list(input().strip())
s = []; p = []; r = []
for i in range(len(String)):
    if String[i] == "(":
        s.append(i)
    elif String[i] == ")":
        p.append([s.pop(), i])

for i in range(len(p)):
    # [3, 5], [0, 6]
    comb = list(combinations(p, i+1))
    # [3, 5], [0, 6], [[3, 5], [0, 6]]
    for com in comb:
        # (0/(0))
        copystr = String[:]
        for f, s in com:
            copystr[f] = ''
            copystr[s] = ''
        r.append(''.join(map(str, copystr)))

for e in sorted(set(r)):
    print(e)