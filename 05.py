from collections import deque

P = deque(open("/home/kfs/AoC2018/05.txt", "r").readline().strip())
D = dict(
    zip(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    )
)


def react(poly, rem=""):
    global D
    np = list()
    for nu in poly:
        if nu not in rem:
            if 0 != len(np):
                if nu != D[np[-1]]:
                    np.append(nu)
                else:
                    np.pop()
            else:
                np.append(nu)
    return len(np)


print(f"Part 1: {react(P)}")
print(f"Part 2: {min(react(P, ch + D[ch]) for ch in 'abcdefghijklmnopqrstuvwxyz')}")
