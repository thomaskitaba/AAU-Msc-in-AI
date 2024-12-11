#!/usr/bin/python3
graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gondar", "Mekele"],
    "Hawassa": [],
    "Gondar": ["Mekele"],  # Adding cycle back to "Bahir Dar"
    "Mekele": ["Addis Ababa", "Gondar"]  # Cycle back to "Addis Ababa"
}

# Initialize the visited and in_path dictionaries
visited = {node: False for node in graph.keys()}
visited = set()
on_path = []

connection = []

def dfs(at, connection):
    if at in visited:
        return
    visited.add(at)
    on_path.append(at)
    print(at)
    
    for city in graph[at]:
        if city not in visited:
            if dfs(city, connection):
                return
        elif city in on_path:
            connection.append([on_path.index(city):])
            return True
    return connection

print(dfs("Addis Ababa", []))



