#!/usr/bin/python3 
from collections import deque


def bfs(start, end, graph):
    
    path = []
    queue = deque([[start, 0, path]])
    n = len(graph.keys())
    visited = set()
    while queue:
        
        # Code goes here    
        current_node, steps, path = queue.popleft()
        if current_node == end:
            print(f"{end} found after {steps} steps")
            return
        visited.add(current_node)
        path.append(current_node)
        
        # visit negbors of current_node
        for negbor in graph[current_node]:
            if negbor not in visited:
                visited.add(negbor)
                print(negbor)
                
                queue.append([negbor, steps + 1, path + [negbor]])
                
        # Visit neighbors of current_node
        # for neighbor in graph[current_node]:
        #     if neighbor not in visited:
        #         visited.add(neighbor)
        #         # Add neighbor to queue with incremented steps
        #         queue.append((neighbor, steps + 1))
    print(f"No path found from {start} to {end}")
    print(path)
    return None
    


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
    end = "Mekele"
    
    bfs(start, end, graph)
    