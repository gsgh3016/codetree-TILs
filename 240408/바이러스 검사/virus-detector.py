import sys


input = sys.stdin.readline
n = int(input())
rest = list(map(int, input().split()))
leader, member = map(int, input().split())

total = 0
for guest in rest:
    total += 1
    if guest > leader:
        num_of_member = (guest - leader) // member
        total += num_of_member + (0 if num_of_member * member == guest - leader else 1)

print(total)