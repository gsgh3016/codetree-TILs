import sys


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = {}
ans = 1
j = 0
for i in range(n):
    while j < n and cnt.get(arr[j], 0) < 1:
        cnt[arr[j]] = cnt.get(arr[j], 0) + 1
        j += 1
    cnt[arr[i]] -= 1
    # print(i, j, cnt)
    ans = max(ans, j - i)
print(ans)