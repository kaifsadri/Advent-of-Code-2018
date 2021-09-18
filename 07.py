from collections import defaultdict

P = [(line.split()[1], line.split()[-3]) for line in open("/home/kfs/AoC2018/07.txt").readlines()]
Steps = defaultdict(set)
for line in P:
    Steps[line[1]].add(line[0])

avail = {line[0] for line in P} - {line[1] for line in P}
done = set()
order = ""
while t := avail - done:
    m = min(t)
    order += m
    done.add(m)
    avail = avail.union({s for s in Steps if Steps[s].issubset(done)})
print(f"Part 1: {order}")

Dur = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(61, 61 + 26)))
avail = {line[0] for line in P} - {line[1] for line in P}
done = set()
t = 0
inwork = dict()
while len(done) < 26:
    while avail and len(inwork) < 5:
        m = min(avail)
        avail.remove(m)
        inwork[m] = Dur[m]
    for worker in inwork.copy():
        inwork[worker] -= 1
        if inwork[worker] == 0:
            del inwork[worker]
            done.add(worker)
    t += 1
    avail = avail.union({s for s in Steps if Steps[s].issubset(done)}) - set(inwork) - done

print(f"Part 2: {t}")
