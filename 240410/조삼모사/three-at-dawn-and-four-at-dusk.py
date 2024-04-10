from itertools import combinations, permutations
import sys


n = int(input())
work = []
for _ in range(n):
    work.append(list(map(int, input().split())))
idx = [i for i in range(n)]
min_dif = 0xff
for comb in combinations(idx, n // 2):
    morning, evening = 0, 0
    evening_comb = [i for i in range(n) if i not in comb]
    for i, j in combinations(comb, 2):
        morning += work[i][j] + work[j][i]
    for i, j in combinations(evening_comb, 2):
        evening += work[i][j] + work[j][i]
    min_dif = min(abs(morning - evening), min_dif)

print(min_dif)