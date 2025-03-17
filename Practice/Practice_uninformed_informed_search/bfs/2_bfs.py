#!/usr/bin/python3
from collections import deque

def bfs(at, goal):
    path = []
    queue = deque([[at, 0, path]])
    visited = set()
    
    while queue:
        
        current_node, steps, path = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
     
        # if current_node not in visited:
        path.append(current_node)
        if current_node == goal:
            print(f"step->{steps}  path-> {path}")
            return       
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited: # we can change this to if not in queue
                queue.append([neighbor, steps + 1, path])
    
    # print(visited)
    return
if __name__ == "__main__":
    graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gondar", "Mekele"],
    "Hawassa": [],
    "Gondar": ["Mekele"],
    "Mekele": ["Addis Ababa", "Gonder"]
    }
    start = "Addis Ababa"
    end = "Adama"
    
    bfs(start, end)
    