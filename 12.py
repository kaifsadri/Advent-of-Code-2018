P = [line for line in open("/home/kfs/AoC2018/12.txt").readlines()]
pots = tuple(i for i, _ in enumerate(P[0].split()[2].strip()) if _ == "#")
T = dict()
for l in P[2:]:
    s = l.strip().split(" => ")
    T[s[0]] = s[1]

l = sum(pots)
last = [0] * 10
g = 0
while True:
    g += 1
    np = list()
    for i in range(min(pots) - 2, max(pots) + 3):
        t = "".join("#" if i + k in pots else "." for k in [-2, -1, 0, 1, 2])
        if T[t] == "#":
            np.append(i)
    pots = tuple(np)
    s = sum(pots)
    delta = s - l
    l = s
    if g == 20:
        print(f"Part 1: {s}")
    last[g % 10] = delta
    if last == [delta] * 10:  # if a pattern repeats 10 times, stop and calculate using that
        break

# s will be the starting point and delta is gonna be added to s for each generation after g
print(f"Part 2: {(50000000000 - g) * delta + s}")
