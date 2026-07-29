"""
Water jug problem, explored level by level with BFS.

State = (a, b): current water level in jug A and jug B.
Capacities: jug A holds CAP_A, jug B holds CAP_B.

successors(state) returns every state reachable in ONE of the six classic
operations:
    1. Fill A completely
    2. Fill B completely
    3. Empty A
    4. Empty B
    5. Pour A -> B (until A empty or B full)
    6. Pour B -> A (until B empty or A full)

We BFS from (0, 0) and print how many *new* states appear at each level.
"""

# LAB 1: state space of the Water Jug problem
# A state is (x, y) = litres in the 4L jug and the 3L jug.

def successors(state):
    x, y = state
    pour_x_to_y = min(x, 3 - y)     # X gives what it has, Y takes what fits
    pour_y_to_x = min(y, 4 - x)     # Y gives what it has, X takes what fits
    return [(4, y),                              # 1. Fill X
            (x, 3),                              # 2. Fill Y
            (0, y),                              # 3. Empty X
            (x, 0),                              # 4. Empty Y
            (x - pour_x_to_y, y + pour_x_to_y),  # 5. Pour X into Y
            (x + pour_y_to_x, y - pour_y_to_x)]  # 6. Pour Y into X


start    = (0, 0)
seen     = {start}      # EVERY state ever found (a set)
frontier = [start]      # states found at the current level
level    = 0

while frontier and level < 8:
    new = []
    for s in frontier:
        for ns in successors(s):
            if ns not in seen:            # <-- the line that matters
                seen.add(ns)
                new.append(ns)
                if ns[0] == 2:
                    print("   *** GOAL: 2L in X at level", level + 1, "***")

    level += 1
    print("Level", level, "->", len(new), "new states:", sorted(new))
    frontier = new          # what we just found becomes what we expand next

print("Total states found:", len(seen))