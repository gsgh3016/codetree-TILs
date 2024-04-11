import sys


def lotate():
    global n
    last = moving_walk[-1]
    for i in range(2 * n - 1, 0, -1):
        moving_walk[i] = moving_walk[i - 1]
        if i <= n - 1:
            people[i] = people[i - 1]
    moving_walk[0] = last
    people[0] = False

def move():
    global n, unstable
    for i in range(n - 1, 0, -1):
        if people[i - 1] and not people[i] and moving_walk[i] > 0:
            people[i] = people[i - 1]
            people[i - 1] = False
            moving_walk[i] -= 1
            if moving_walk[i] == 0:
                unstable += 1
    people[0] = False

def one_more():
    global unstable
    if moving_walk[0] > 0 and not people[0]:
        people[0] = True
        moving_walk[0] -= 1
        if moving_walk[0] == 0:
            unstable += 1


n, k = map(int, input().split())
moving_walk = list(map(int, input().split()))
l = len(moving_walk)
people = [False for _ in range(n)]
unstable = 0
experiment = 0

while unstable < k:
    experiment += 1
    lotate()
    move()
    one_more()

print(experiment)