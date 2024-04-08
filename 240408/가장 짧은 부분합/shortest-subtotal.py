import sys


input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

j = 0
min_len = n
acc = 0
for i in range(n):
    while j < n - 1 and acc < s:
        acc += arr[j]
        j += 1
    acc -= arr[i]
    min_len = min(min_len, j - i + 1)
print(min_len)