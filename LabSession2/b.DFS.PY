# LAB 2b: Depth-First Search
graph = {'A': ['B','C'],
         'B': ['D','E'],
         'C': ['F','G'],
         'D': [],  'E': ['H'],
         'F': [],  'G': [],  'H': []}
def dfs(start, goal):
    stack   = [[start]]         # same structure as BFS
    visited = []
    while stack:
        path = stack.pop()      # <-- LIFO: take from the END
        node = path[-1]
        if node == goal:
            return path, visited
        if node not in visited:
            visited.append(node)
            for n in reversed(graph[node]):   # reverse: left child on top
                stack.append(path + [n])
    return None, visited
p, v = dfs('A', 'H')
print("DFS path   :", p)
print("DFS visited:", v)
