# LAB 3: Uniform Cost Search
# The graph now stores (neighbour, cost) pairs.
graph = {'A': [('B',1), ('C',4)],
         'B': [('D',5), ('C',2)],
         'C': [('D',1)],
         'D': []}
def ucs(start, goal):
    queue = [(0, [start])]       # (accumulated cost, path)
    while queue:
        queue.sort()             # cheapest path first
        cost, path = queue.pop(0)
        if path[-1] == goal:     # goal test on POP, never on generate
            return cost, path
        for n, w in graph[path[-1]]:
            queue.append((cost + w, path + [n]))
    return None
print("UCS:", ucs('A', 'D'))
