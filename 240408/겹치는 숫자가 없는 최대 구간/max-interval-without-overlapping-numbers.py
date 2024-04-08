import sys


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = {}
for i in arr:
    if i not in cnt:
        cnt[i] = 0
ans = 0
j = 0
for i in range(n):
    while j < n - 1 and cnt[arr[j]] <= 1:
        cnt[arr[j]] += 1
        j += 1
    cnt[arr[i]] -= 1
    # print(i, j, cnt)
    ans = max(ans, j - 1 - i)
print(ans)