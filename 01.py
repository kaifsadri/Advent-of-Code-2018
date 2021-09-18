p = list(int(i.strip()) for i in open("/home/kfs/AoC2018/01.txt", "r").readlines())

print(f"Part 1: {sum(p)}")

H = set()
f = 0
i = 0
while f not in H:
    H.add(f)
    f += p[i % len(p)]
    i += 1
print(f"Part 2: {f}")
