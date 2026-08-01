# LAB 2a: Breadth-First Search
graph = {'A': ['B','C'],
         'B': ['D','E'],
         'C': ['F','G'],
         'D': [],  'E': ['H'],
         'F': [],  'G': [],  'H': []}
def bfs(start, goal):
    queue   = [[start]]     # a list of PATHS, not nodes
    visited = []
    while queue:
        path = queue.pop(0)     # <-- FIFO: take from the FRONT
        node = path[-1]         # current node = last item of the path
        if node == goal:
            return path, visited
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                queue.append(path + [n])
    return None, visited
p, v = bfs('A', 'H')
print("BFS path   :", p)
print("BFS visited:", v)