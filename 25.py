P = {tuple(map(lambda x: int(x), line.split(","))) for line in open("/home/kfs/AoC2018/25.txt").readlines()}


def close(a, b):
    return sum(abs(a[i] - b[i]) for i in range(4)) <= 3


C = 0
while P:
    const = {P.pop()}
    while const:
        s = const.pop()
        for star in P.copy():
            if close(star, s):
                P.remove(star)
                const.add(star)
    C += 1

print(f"Part 1: {C}")
