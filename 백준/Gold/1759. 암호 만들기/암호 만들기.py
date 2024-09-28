import sys, itertools
input = sys.stdin.readline

L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()

result = []
for comb in itertools.combinations(lst, L):
    vowel, constant = 0, 0
    for c in comb:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            constant += 1
    if vowel >= 1 and constant >= 2:
        result.append(''.join(map(str, comb)))

for r in result:
    print(r)