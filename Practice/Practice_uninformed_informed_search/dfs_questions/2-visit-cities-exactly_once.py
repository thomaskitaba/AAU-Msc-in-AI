#!/usr/bin/python3
import sys
sys.path.append('../Practice')  # Adds the parent directory to the module search path

from graph import graph
"""
o	Question: "Use Depth-First Search (DFS) to find a route from 'Addis Ababa' to 'Hawassa'."
o	Objective: Explore all possible paths from Addis Ababa to Mekele, and report if a path exists.
o              NOTE:  your adversary is residing on gonder so dont pass through gonder
"""

visited = []
all_paths = [] 
count = 0

def fill_path(visited, total_distance):
	if visited not in [path[0] for path in all_paths]:
		info = []
		info.append(list(visited))
		# info.append (f'{total_distance} km')
		info.append(total_distance)
		all_paths.append(info)
		# all_paths.append(list(visited))
    
def dfs(current_city,  total_distance):
	if current_city in visited:
		return
	visited.append(current_city)
  
	for city, data in graph.get(current_city).items():
		dfs(city, total_distance + data["distance"])
	
	fill_path(visited, total_distance)
	visited.pop()
	
start = "Addis Ababa"
statistics = []

# dfs(start, 0)
# print(all_paths)

    
max_distance = []
for city in graph.keys():
    # all_paths.append(["============================="])
    dfs(city, 0)
    
for path_info in all_paths:
	print(path_info)
	max_distance.append(path_info[1])
	# statistics.append([path_info[0][0], max_path])
# print(statistics)
print(f'maximum distance that can be traveled  => {max(max_distance)}')

# Find the maximum distance that can be traveled by the sales man starting from any location


    
