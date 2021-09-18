from collections import Counter

p = [line.strip() for line in open("/home/kfs/AoC2018/02.txt", "r").readlines()]

N2 = N3 = 0
for l in p:
    C = Counter(l)
    if 2 in C.values():
        N2 += 1
    if 3 in C.values():
        N3 += 1

print(f"Part 1: {N2 * N3}")


def comm(s1, s2):
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
    return result


flag = False
for m in range(len(p)):
    if flag:
        break
    for n in range(m, len(p)):
        if len(d := comm(p[m], p[n])) == len(p[m]) - 1:
            print(f"Part 2: {d}")
            flag = True
            break
