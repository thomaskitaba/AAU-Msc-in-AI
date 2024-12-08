#!/usr/bin/python3

# g = adjecency list 
# visited = nodes visited
# n = number of nodes


graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4],
    6: [7],
    7: [6, 8],
    8: [7, 9],
    9: [8],
    10: []
}
graph2 = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1],
    4: [1, 5, 6],
    5: [2, 4],
    6: [4]
}
components= []
component = []

visited = dict([val, False] for val in graph)
# print(visited)
visited = set()

def dfs(at, component):
    if at in visited:
        return
    visited.add(at)
    # print(at, end=" ")
    
    component.append(at)
    # dig deepeer
    for ng in graph[at]:
        if ng not in visited:
            dfs(ng, component)
    return component
    
# dfs(6)
for node in graph:
    if node not in visited:
        components.append(dfs(node, []))
print(f'{len(components)} -> separate components')
for component in components:
    print(component)

