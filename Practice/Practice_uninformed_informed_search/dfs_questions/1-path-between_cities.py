#!/usr/bin/python3
import sys
sys.path.append('../Practice')  # Adds the parent directory to the module search path

from graph import graph
"""
o	Question: "Use Depth-First Search (DFS) to find a route from 'Addis Ababa' to 'Hawassa'."
o	Objective: Explore all possible paths from Addis Ababa to Mekele, and report if a path exists.
o              NOTE:  your adversary is residing on gonder so dont pass through gonder
"""

visited = set()
all_paths = [] 
danger_route = []
count = 0

def dfs(current_city, destination, danger, rec_path, total_distance):
    if current_city not in rec_path:
        rec_path.append(current_city)
    if current_city == danger:
        rec_path.pop()
        return
    if current_city == destination:
        info = {}
        info["Path"] = list(rec_path)
        info["Distance"] = total_distance
        all_paths.append(info)
        rec_path.pop()
        return
    
    # for key, value in graph.items():
    for city, data in graph.get(current_city).items():
        dfs(city, destination, danger, rec_path, total_distance + data["distance"])
        
    rec_path.pop()
    
start = "Addis Ababa"
end = "Mekele"
danger = "Safe"

dfs(start, end, danger,  [], 0)

for count, path in enumerate(all_paths):
   for key, val in path.items():
        info = ''
        if type(val) is list:
            info += key + f"  {count}" + '  ' + '->'.join(val) 
            print(info, end="")
        else:
            print(f'  Total distance {val}')


