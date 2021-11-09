# part 1:
Board = [3, 7]
elf1, elf2 = 0, 1
target = 320851

while True:
    new_recipe = Board[elf1] + Board[elf2]
    if new_recipe >= 10:
        Board.append(1)
        if len(Board) == target + 10:
            print("Part 1: ", "".join(str(x) for x in Board[-10:]))
            break
    Board.append(new_recipe % 10)
    if len(Board) == target + 10:
        print("Part 1: ", "".join(str(x) for x in Board[-10:]))
        break
    elf1 = (elf1 + Board[elf1] + 1) % len(Board)
    elf2 = (elf2 + Board[elf2] + 1) % len(Board)

# Part 2
Board = [3, 7]
elf1, elf2 = 0, 1
target = [
    3,
    2,
    0,
    8,
    5,
    1,
]
while True:
    new_recipe = Board[elf1] + Board[elf2]
    if new_recipe >= 10:
        Board.append(1)
        if Board[-len(target) :] == target:
            print("Part 2: ", len(Board) - len(target))
            break
    Board.append(new_recipe % 10)
    if Board[-len(target) :] == target:
        print("Part 2: ", len(Board) - len(target))
        break
    elf1 = (elf1 + Board[elf1] + 1) % len(Board)
    elf2 = (elf2 + Board[elf2] + 1) % len(Board)
