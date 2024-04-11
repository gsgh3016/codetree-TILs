import sys


ADD = 0
SUB = 1
MUL = 2

def cal(a, b, op):
    if op == ADD:
        return a + b
    elif op == SUB:
        return a - b
    elif op == MUL:
        return a * b

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
dp1 = [[0, 0, 0, 0] for _ in range(n)]
dp2 = [[0, 0, 0, 0] for _ in range(n)]
dp1[0] = [nums[0], *ops]
dp2[0] = [nums[0], *ops]

for i in range(1, n):
    cur_min = dp2[i - 1][0] * nums[i] if dp2[i - 1][0] > 0 else dp2[i - 1][0] + nums[i]
    min_op_idx = -1
    cur_max = dp1[i - 1][0] * nums[i] if dp1[i - 1][0] < 0 else dp1[i - 1][0] - nums[i]
    max_op_idx = -1

    for j in range(1, 4):
        if dp1[i - 1][j] > 0 and cal(dp1[i - 1][0], nums[j], j - 1) < cur_min:
            cur_min = cal(dp1[i - 1][0], nums[i], j - 1)
            min_op_idx = j
        if dp2[i - 1][j] > 0 and cal(dp2[i - 1][0], nums[j], j - 1) > cur_max:
            cur_max = cal(dp2[i - 1][0], nums[i], j - 1)
            max_op_idx = j
    
    dp1[i][0] = cur_min
    dp2[i][0] = cur_max
    for j in range(1, 4):
        if j == min_op_idx:
            dp1[i][j] = dp1[i - 1][j] - 1
        else:
            dp1[i][j] = dp1[i - 1][j]
        
        if j == max_op_idx:
            dp2[i][j] = dp2[i - 1][j] - 1
        else:
            dp2[i][j] = dp2[i - 1][j]

print(dp1[n - 1][0], dp2[n - 1][0])