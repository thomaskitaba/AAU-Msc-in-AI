#!/usr/bin/python3
"""
detect cycle in a graph
"""
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [0]
}
visited = {node: False for node in graph.keys()}
in_path = {node: False for node in graph.keys()} # To find cycle
def dfs(at):
    if in_path[at]:
        print(f"Cycle Found at {at}")
        return
    if visited[at]:
        return
    
    visited[at] = 1
    in_path[at] = 1

    neighbor = graph[at]
    for sibling in neighbor:
        dfs(sibling)
    in_path[at] = 0

if __name__ == "__main__":
    
    for node in graph.keys():
        # if visited[node]:
        dfs(node)
    