import sys


input = sys.stdin.readline
n = int(input())
rest = list(map(int, input().split()))
leader, member = map(int, input().split())

total = 0
for guest in rest:
    total += 1 + (guest - leader) // member + 1

print(total)