import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())
lst = ['a', 'e', 'i', 'o', 'u']
array = list(map(str, input().split()))
array.sort()

result = []
for comb in combinations(array, L):
    vowel_cnt = 0
    consonant_cnt = 0
    for i in comb:
        if i in lst:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        result.append("".join(map(str, comb)))

result.sort()
for i in result:
    print(i)