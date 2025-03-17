#!/usr/bin/python3
"""
General Alghoritm for DFS  that works both for 
directed and Undireted graph
"""
# TODO: Global scope variables
# Adjesencey list representing the graph
graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gonder", "Mekele"],
    "Hawassa": [],
    "Gonder": ["Mekele"],
    "Mekele": ["Addis Ababa", "Gonder"]
}

# n =   (number of nodes)
n = len(graph)
# Visited = [false, false...]  #size = n
visited = dict([i, 0] for i in graph.keys())
name = []

shortest_step = float("infinity")
destination = "Mekele"

def dfs(current_node, steps):
    global shortest_step
    # base Case
    if visited.get(current_node):
        return
   
    if (current_node) == destination:
        shortest_step = min(steps, shortest_step)

    visited[current_node] = 1
    name.append(current_node)
    for city in graph[current_node]:
        dfs(city, steps + 1)
    visited[current_node] = 0
    
dfs("Addis Ababa", 0)
print(name)
print(f"shortest step: {shortest_step}")
