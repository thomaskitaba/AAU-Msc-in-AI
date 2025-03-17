#!/usr/bin/python3
print("Thomas Kitaba")

graph = {
    'Addis Ababa': ['Ambo', 'Adama', 'Debre Berhan', 'Holeta'],
    'Ambo': ['Addis Ababa', 'Woliso'],
    'Adama': ['Addis Ababa', 'Assella', 'Batu'],
    'Debre Berhan': ['Addis Ababa', 'Debre Sina'],
    'Holeta': ['Addis Ababa'],
    'Woliso': ['Ambo', 'Jimma'],
    'Jimma': ['Woliso', 'Bonga'],
    'Bonga': ['Jimma', 'Gore'],
    'Gore': ['Bonga', 'Gambela'],
    'Gambela': ['Gore'],
    'Assella': ['Adama', 'Dodola'],
    'Dodola': ['Assella', 'Bale'],
    'Bale': ['Dodola', 'Goba'],
    'Goba': ['Bale', 'Liben'],
    'Liben': ['Goba', 'Moyale'],
    'Moyale': ['Liben'],
    'Batu': ['Adama', 'Shashemene', 'Arsi Negele'],
    'Shashemene': ['Batu', 'Awasa'],
    'Awasa': ['Shashemene', 'Dilla'],
    'Dilla': ['Awasa', 'Yabelo'],
    'Yabelo': ['Dilla', 'Konso'],
    'Konso': ['Yabelo', 'Arba Minch'],
    'Arba Minch': ['Konso'],
    'Debre Sina': ['Debre Berhan', 'Kemise'],
    'Kemise': ['Debre Sina', 'Dessie'],
    'Dessie': ['Kemise', 'Woldia'],
    'Woldia': ['Dessie', 'Lalibela'],
    'Lalibela': ['Woldia', 'Sekota'],
    'Sekota': ['Lalibela', 'Axum'],
    'Axum': ['Sekota', 'Shire'],
    'Shire': ['Axum', 'Humera'],
    'Humera': ['Shire', 'Kartu'],
    'Kartu': ['Humera'],
}

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}
class UninformedSearch:
    """
    Uninformed Depth First Search to go from start city to a goal city.
    """
    def __init__(self, graph, goal):
        self.graph = graph
        self.visited = {node: False for node in graph}
        self.goal = goal
        self.path = []  # To store the path to the goal
    
    def dfs(self, current_node):
        # Base case: if the current node is the goal, return True
        if current_node == self.goal:
            self.path.append(current_node)
            print(self.path)
            return True
        
        # If already visited, return False
        if self.visited[current_node]:
            return False
        # Mark the current node as visited
        self.visited[current_node] = True
        # print(self.visited)
        # Recur for all neighbors
        for neighbor in self.graph.get(current_node, []):
            if self.dfs(neighbor):  # If goal found in a neighbor's DFS, stop
                self.path.append(current_node)  # Add current node to the path
                return True
        # If no path is found to the goal, return False
        return False

# Test the search


start_city = "A"
goal_city = "D"

my_graph = UninformedSearch(graph, goal_city)
if my_graph.dfs(start_city):
    print("Path to the goal:", list(reversed(my_graph.path)))  # Reverse the path to get start -> goal
else:
    print("No path found to the goal.")
