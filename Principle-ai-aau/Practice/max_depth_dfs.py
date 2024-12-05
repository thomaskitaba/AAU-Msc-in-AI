#!/usr/bin/python3
graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gonder", "Mekele"],
    "Hawassa": [],
    "Gonder": ["Mekele"],
    "Mekele": ["Addis Ababa", "Gonder"]
}
depths = []
start_node = [key for key in graph.keys()][0]
visited = {key: 0 for key in graph.keys()}
in_path = {key: 0 for key in graph.keys()}

def dfs(at, depth):
    if visited[at] == 1:
        depth -= 1
        return 
    if in_path[at] == 1:
        return 
    depth += 1
    visited[at] = 1
    in_path[at] = 1
    
    for city in graph[at]:
        depth = dfs(city, depth + 1)
    
    in_path[at] = 0
    depths.append(depth)

dfs(start_node, 0)
print(max(depths))
    