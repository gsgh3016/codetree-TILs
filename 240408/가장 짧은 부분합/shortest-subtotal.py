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
    ans = min(ans, j - i + 1)
print(ans)