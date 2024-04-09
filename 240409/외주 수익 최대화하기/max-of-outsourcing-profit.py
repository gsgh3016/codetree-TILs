import sys


input = sys.stdin.readline
n = int(input())
time = [0 for _ in range(n + 1)]
price = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    time[i], price[i] = map(int, input().split())

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    if i + time[i] - 1 <= n:
        dp[i + time[i] - 1] = max(dp[i + time[i] - 1], dp[i - 1] + price[i])

print(dp[n])