#!/usr/bin/python3


graph = {
    "Addis Ababa": {
        "Adama": {"distance": 598, "heuristic": 50},
        "Bahir Dar": {"distance": 225, "heuristic": 150},
    },
    "Adama": {
        "Hawassa": {"distance": 164, "heuristic": 150},
    },
    "Bahir Dar": {
        "Gondar": {"distance": 378, "heuristic": 350},
        "Mekele": {"distance": 644, "heuristic": 300},
        
    },
    "Hawassa": {},
    "Gondar": {
        "Mekele": {"distance": 273, "heuristic": 280},
    },
    "Mekele": {
        "Addis Ababa": {"distance": 447, "heuristic": 400},
    },
}

graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gondar", "Mekele"],
    "Hawassa": [],
    "Gondar": ["Mekele"],  # Adding cycle back to "Bahir Dar"
    "Mekele": ["Addis Ababa", "Gondar"]  # Cycle back to "Addis Ababa"
}
visited = set()
count = 0
# rec_path = []
cycles = []


def dfs(current_city, rec_path):
    # print(current_city)
    
    if current_city in rec_path:
        visited_index = rec_path.index(current_city)
        cycle = rec_path[visited_index:] + [current_city]
    
        if sorted(cycle) not in [sorted(c) for c in cycles]:
            cycles.append(cycle)
        return
    
    if current_city  in visited:
        return
    
    visited.add(current_city)
    rec_path.append(current_city)
    
    for city in graph.get(current_city, {}):
        # if city not in visited:   #todo: if this is uncomented cycles wont be detected, because the city where the cycle occurs wont be passed to the "if current_city in rec_path:
        dfs(city, rec_path)    
    rec_path.pop()
  
if __name__ == "__main__":
    start = [city for city in graph.keys()][0]

    print(f'Cities:- {len(visited)}')

    # print(cycles)
    
    dfs(start, [])
    print(cycles)
    
   