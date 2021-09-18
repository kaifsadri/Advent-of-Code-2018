puz = [line.strip() for line in open("/home/kfs/AoC2018/10.txt").readlines()]

Screen = 65
P = list()
V = list()

for l in puz:
    px = int(l[10:16])
    py = int(l[18:24])
    vx = int(l[36:38])
    vy = int(l[40:42])
    P.append([px, py])
    V.append((vx, vy))

for t in range(1, 11_000):
    for i, point in enumerate(P):
        P[i] = [P[i][0] + V[i][0], P[i][1] + V[i][1]]
    xmax = max(x[0] for x in P)
    xmin = min(x[0] for x in P)
    ymax = max(x[1] for x in P)
    ymin = min(x[1] for x in P)
    if xmax - xmin > Screen or ymax - ymin > Screen:
        continue
    else:
        # display here:
        print("-" * Screen)
        print(f"After {t} seconds:")
        print("-" * Screen)
        for row in range(ymin, ymax + 1):
            for col in range(xmin, xmax + 1):
                print("█" if [col, row] in P else " ", end="")
            print()
        print("-" * Screen)
