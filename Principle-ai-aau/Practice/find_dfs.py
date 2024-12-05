#!/usr/bin/python3
"""
Find nodes from a graph 
and return how many found
"""

def findNode(graph, target):
    count = [0]
    current_node = [ key for key in graph.keys()][0]
    print(f"start node: {current_node} end node: {target}")
    visited = dict([key, 0] for key in graph)
    paths = []
    path = []
    
    def dfs(current_node, target,path):
       
        # base case
        if visited[current_node] == 1:
            return
        visited[current_node] = 1
        path.append(current_node)
        # path.append(current_node)
        
        if current_node == target:
            paths.append(list(path))
            # path = []
            count[0] += 1
        for city in graph[current_node]:           
            dfs(city, target, path)
        path.pop()
        visited[current_node] = 0
    
    dfs(current_node, target, path)   
    print(count[0])
    print(paths)

if __name__ == "__main__":
       
    
    # Adjesencey list representing the graph
    graph = {
        "Addis Ababa": ["Adama", "Bahir Dar"],
        "Adama": ["Hawassa"],
        "Bahir Dar": ["Gondar", "Mekele"],
        "Hawassa": [],
        "Gondar": ["Mekele"],
        "Mekele": []
    }
    target = "Mekele"
    result = findNode(graph, target)
    # print(result)
    # print(graph)
    graph = {
    "Addis Ababa": [{"Adama": 100}, {"Bahir Dar": 200}],
    "Adama": [{"Hawassa": 400}],
    "Bahir Dar": [{"Gondar": 230}, {"Mekele": 400}],
    "Hawassa": [],
    "Gondar": [{"Mekele": 300}],
    "Mekele": []
    }