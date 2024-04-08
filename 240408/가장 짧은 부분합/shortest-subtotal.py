import sys


input = sys.stdin.readline
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

j = 0
ans = n
acc = 0
for i in range(1 + n):
    while j <= n and acc < s:
        acc += arr[j]
        j += 1
    acc -= arr[i]
    if acc >= s:
        ans = min(ans, j - 1 - i)
    # print(i, j, acc, ans)
print(ans)