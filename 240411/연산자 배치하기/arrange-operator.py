import sys


input = sys.stdin.readline

min_val = 0xffffffff
max_val = -0xffffffff

def find(i, a, s, m, res):
    global n, min_val, max_val
    if i == n - 1:
        min_val, max_val = min(min_val, res), max(max_val, res)
        return

    if a > 0:
        find(i + 1, a - 1, s, m, res + nums[i + 1])
    if s > 0:
        find(i + 1, a, s - 1, m, res - nums[i + 1])
    if m > 0:
        find(i + 1, a, s, m - 1, res * nums[i + 1])

n = int(input())
nums = list(map(int, input().split()))
add, sub, mul = map(int, input().split())
find(0, add, sub, mul, nums[0])
print(min_val, max_val)