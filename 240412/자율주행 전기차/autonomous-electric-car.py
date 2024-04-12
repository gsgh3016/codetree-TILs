from queue import PriorityQueue, Queue
import sys


def to_int(s):
    return int(s) - 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

input = sys.stdin.readline
n, m, c = map(int, input().split())
adj_map = []
for _ in range(n):
    adj_map.append(list(map(int, input().split())))
rx, ry = map(to_int, input().split())
passenger = set()
path = {}
for i in range(2, m + 2):
    sx, sy, ex, ey = map(to_int, input().split())
    passenger.add((sx, sy))
    path[(sx, sy)] = (ex, ey)


def find_new_passenger(rx, ry):
    global n, c
    if c == -1:
        return -1, -1, -1
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = Queue()
    res = PriorityQueue()
    visited[rx][ry] = True
    q.put((rx, ry, 0))
    if (rx, ry) in passenger:
        return rx, ry, c

    while not q.empty():
        cx, cy, cd = q.get()
        for i in range(4):
            nx, ny, nd = cx + dx[i], cy + dy[i], cd + 1
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or adj_map[nx][ny] == 1:
                continue
            if (nx, ny) in passenger and c - nd >= 0:
                res.put((nd, nx, ny))
            visited[nx][ny] = True
            q.put((nx, ny, nd))

    if res.empty():
        return -1, -1, -1
    nearest = res.get()
    return nearest[1], nearest[2], c - nearest[0]


def go_destination(rx, ry, ex, ey):
    global n, c
    if c == -1 or (ex, ey) == (-1, -1):
        return -1
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = Queue()
    visited[rx][ry] = True
    q.put((rx, ry, 0))

    while not q.empty():
        cx, cy, cd = q.get()
        for i in range(4):
            nx, ny, nd = cx + dx[i], cy + dy[i], cd + 1
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or adj_map[nx][ny] == 1:
                continue
            if (nx, ny) == (ex, ey):
                return c + nd
            if c - nd < 0:
                return -1
            visited[nx][ny] = True
            q.put((nx, ny, nd))
    
    return -1


for _ in range(m):
#    print(f"cur: {rx, ry}, battery: {c}")
    for src in passenger:
        print(f"{src} -> {path[src]}")
    gx, gy, c = find_new_passenger(rx, ry)
#    print(f"move to priority: {gx, gy}, battery: {c}")
    gdx, gdy = path[(gx, gy)] if (gx, gy) in path else (-1, -1)
    c = go_destination(gx, gy, gdx, gdy)
#    print(f"nearest passenger: {gx, gy} -> {gdx, gdy}, battery: {c}")
    rx, ry = gdx, gdy
    passenger.discard((gx, gy))

print(c)