from collections import deque, defaultdict


def play(part):
    # Input: 476 players; last marble is worth 71657 points
    lastmarble = 71657 if part == 1 else 7165700
    players = 476
    circle = deque([0])
    marble = 1
    elves = defaultdict(int)
    M = 0
    while marble < lastmarble:
        if marble % 23 != 0:
            circle.rotate(-2)
            circle.appendleft(marble)
        else:
            circle.rotate(7)
            m = marble % players
            elves[m] += marble + circle.popleft()
            M = max(M, elves[m])
        marble += 1
    return M


print(f"Part 1: {play(1)}")
print(f"Part 2: {play(2)}")
