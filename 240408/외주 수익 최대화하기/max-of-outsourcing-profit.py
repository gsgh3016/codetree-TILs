import sys


input = sys.stdin.readline
n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0 for _ in range(n + 1)]
for i in range(n):
    if i + t[i] <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])
    
print(dp[n])