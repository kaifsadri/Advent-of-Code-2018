P = [int(i) for i in open("08.txt", "r").readline().split()]


def tree1(start):
    global P
    children = P[start]
    metadata = P[start + 1]
    init = start + 2
    result = [0, 0]
    if children == 0:
        result = [sum(P[init : init + metadata]), init + metadata]
    else:
        for i in range(children):
            r = tree1(init)
            result[0] += r[0]
            init = r[1]
        result[0] += sum(P[init : init + metadata])
        result[1] = init + metadata
    return result


print("Part 1: ", tree1(0)[0])


def tree2(start):
    global P
    children = P[start]
    metadata = P[start + 1]
    init = start + 2
    result = [0, 0, 0]
    if children == 0:
        result = [sum(P[init : init + metadata]), init + metadata]
    else:
        kids = list()
        for i in range(children):
            r = tree2(init)
            kids.append(r[0])
            init = r[1]
        for child in range(init, init + metadata):
            if P[child] <= children:
                result[0] += kids[P[child] - 1]
        result[1] = init + metadata
    return result


print("Part 2: ", tree2(0)[0])
