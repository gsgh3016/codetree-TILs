import sys


input = sys.stdin.readline
l, q = map(int, input().split())
query = {}


def take_picture(t: int):
    people_num = len(query)
    chobap_num = 0
    for name, qu in query.items():
        if 200 not in qu:
            chobap_num += 1
            people_num -= 1
            continue
        t_s, x_s, n = qu[200]
        for t_c, x_c in qu[100]:
            if x_c + t - t_c >= l or (t_s - t_c + x_c) % l == x_s:
                n -= 1
        if n == 0:
            people_num -= 1
        chobap_num += n
    print(people_num, chobap_num)

for _ in range(q):
    cmd = input().split()
    if cmd[0] == "100":
        query.setdefault(cmd[3], {}).setdefault(100, []).append(list(map(int, [cmd[1], cmd[2]])))
    if cmd[0] == "200":
        query[cmd[3]][200] = list(map(int, [cmd[1], cmd[2], cmd[4]]))
    if cmd[0] == "300":
        # for name, cmd_sort in query.items():
        #     for code, contents in cmd_sort.items():
        #         print(name, code, contents)
        take_picture(int(cmd[1]))