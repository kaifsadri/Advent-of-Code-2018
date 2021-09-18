from collections import defaultdict

p = [line.split() for line in open("/home/kfs/AoC2018/03.txt", "r").readlines()]

Fabric = defaultdict(set)
Claims = set()

for l in p:
    claim = int(l[0][1:])
    Claims.add(claim)
    st = tuple(int(i) for i in l[2][:-1].split(","))
    sz = tuple(int(i) for i in l[3].split("x"))
    for x in range(st[0], st[0] + sz[0]):
        for y in range(st[1], st[1] + sz[1]):
            Fabric[(x, y)].add(claim)
print(f"Part 1: {sum(1 for i in Fabric if len(Fabric[i])>1)}")

for sqin in Fabric:
    if len(c := Fabric[sqin]) > 1:
        Claims -= c
print(f"Part 2: {Claims.pop()}")
