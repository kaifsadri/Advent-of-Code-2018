from collections import defaultdict

L = sorted(line.strip() for line in open("04.txt").readlines())

DATA = defaultdict(lambda: [0] * 60)
guard = ""

for line in L:
    s = line.split()
    if "Guard" in line:
        guard = s[3]
        continue
    elif "falls" in line:
        minute = int(s[1].split(":")[1][:-1])
        for m in range(minute, 60):
            DATA[guard][m] += 1
    elif "wakes" in line:
        minute = int(s[1].split(":")[1][:-1])
        for m in range(minute, len(DATA[guard])):
            DATA[guard][m] -= 1

target_guard = max(DATA, key=lambda x: sum(DATA[x]))
target_minute = DATA[target_guard].index(max(DATA[target_guard]))
print("Part 1: ", int(target_guard[1:]) * target_minute)

target_guard = max(DATA, key=lambda x: max(DATA[x]))
target_minute = DATA[target_guard].index(max(DATA[target_guard]))
print("Part 2: ", int(target_guard[1:]) * target_minute)
