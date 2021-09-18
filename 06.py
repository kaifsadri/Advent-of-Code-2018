from collections import defaultdict

P = [
    tuple(map(lambda x: int(x), line.strip().split(", ")))
    for line in open("/home/kfs/AoC2018/06.txt").readlines()
]

Areas = defaultdict(set)

xmin = min(s[0] for s in P)
xmax = max(s[0] for s in P)
ymin = min(s[1] for s in P)
ymax = max(s[1] for s in P)
# dmax = abs(xmax - xmin) + abs(ymax - ymin)

for x in range(xmin, xmax + 1):
    for y in range(ymin, ymax + 1):
        d = defaultdict(set)
        for star in P:
            d[abs(star[0] - x) + abs(star[1] - y)].add(star)
        if len(st := d[min(d)]) == 1:
            Areas[st.pop()].add((x, y))

IntStars = set(Areas)
for x in [xmin, xmax]:
    for y in range(ymin, ymax + 1):
        for star in Areas:
            if star in IntStars and (x, y) in Areas[star]:
                IntStars.remove(star)
for y in [ymin, ymax]:
    for x in range(xmin, xmax + 1):
        for star in Areas:
            if star in IntStars and (x, y) in Areas[star]:
                IntStars.remove(star)

print(f"Part 1: {max(len(Areas[i]) for i in IntStars)}")

P2Area = set()
for x in range(xmin, xmax + 1):
    for y in range(ymin, ymax + 1):
        d = list()
        for star in P:
            d.append(abs(star[0] - x) + abs(star[1] - y))
        if sum(d) < 10_000:
            P2Area.add((x, y))
print(f"Part 2: {len(P2Area)}")
