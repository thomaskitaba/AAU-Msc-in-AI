#!/usr/bin/python3
import heapq
# we are going to use minheap(priority queue) to implement bfs
class informedSearch:
    
    def __init__(self, graph):
        self.graph = graph  
        
    def ucs(self, start, goal, path):
        pri_queue = []
        heapq.heappush(pri_queue, (0, start, path))
        
        while pri_queue:
            
            g, current_city, path = heapq.heappop(pri_queue)
            vistied = set()
            if current_city == goal:
                return g, path + [current_city]
            
            if current_city not in vistied:
                vistied.add(current_city)
                new_path = list(path)
                new_path.append(current_city)
                for neighbor, cost in graph.get(current_city, []):
                    heapq.heappush(pri_queue,(g + cost, neighbor, new_path))
        return f"Path from {start} to {goal} not found"

            
            
    

if __name__ == "__main__":
    graph = {
    "Addis Ababa": [("Ambo", 5), ("Adama", 3), ("Debre Berhan", 5)],
    "Ambo": [("Addis Ababa", 5), ("Woliso", 6)],
    "Adama": [("Addis Ababa", 3), ("Assella", 4), ("Batu", 4)],
    "Debre Berhan": [("Addis Ababa", 5), ("Debre Sina", 3)],
    "Holeta": [("Addis Ababa", 1)],
    "Woliso": [("Ambo", 3), ("Jimma", 6)],
    "Jimma": [("Woliso", 6), ("Bonga", 4)],
    "Bonga": [("Jimma", 4), ("Gore", 5)],
    "Gore": [("Bonga", 5), ("Gambela", 6)],
    "Gambela": [("Gore", 6)],
    "Assella": [("Adama", 4), ("Dodola", 3)],
    "Dodola": [("Assella", 3), ("Bale", 4)],
    "Bale": [("Dodola", 4), ("Goba", 6)],
    "Goba": [("Bale", 6), ("Liben", 13)],
    "Liben": [("Goba", 13), ("Moyale", 11)],
    "Moyale": [("Liben", 11)],
    "Batu": [("Adama", 3), ("Shashemene", 4)],
    "Shashemene": [("Batu", 4), ("Hawassa", 3)],
    "Hawassa": [("Shashemene", 3), ("Dilla", 4)],
    "Dilla": [("Hawassa", 4), ("Yabelo", 6)],
    "Yabelo": [("Dilla", 6), ("Konso", 3)],
    "Konso": [("Yabelo", 3), ("Arba Minch", 6)],
    "Arba Minch": [("Konso", 6)],
    "Debre Sina": [("Debre Berhan", 3), ("Kemise", 4)],
    "Kemise": [("Debre Sina", 4), ("Dessie", 3)],
    "Dessie": [("Kemise", 3), ("Woldia", 4)],
    "Woldia": [("Dessie", 4), ("Lalibela", 11)],
    "Lalibela": [("Woldia", 11), ("Sekota", 8)],
    "Sekota": [("Lalibela", 8), ("Axum", 6)],
    "Axum": [("Sekota", 6), ("Shire", 8)],
    "Shire": [("Axum", 8), ("Humera", 7)],
    "Humera": [("Shire", 7), ("Kartum", 21)],
    "Kartum": [("Humera", 21)]
}
    
    
# utitlity expected to reach the goal city from a specific city
    heuristic = {
    "Addis Ababa": 26,
    "Ambo": 31,
    "Adama": 23,
    "Debre Berhan": 31,
    "Holeta": 21, 
    "Woliso": 25,
    "Jimma": 33,
    "Bonga": 13,
    "Gore": 46,
    "Gambela": 51,
    "Assella": 22,
    "Dodola": 19, 
    "Bale": 22, 
    "Goba": 40,
    "Liben": 11, 
    "Moyale": 0,
    "Batu": 19,
    "Shashemene": 16,
    "Hawassa": 15,
    "Dilla": 12,
    "Yabelo": 6,
    "Konso": 9,
    "Arba Minch": 13,
    "Debre Sina": 33,
    "Kemise": 40,
    "Dessie": 44,
    "Woldia": 30,
    "Lalibela": 57,
    "Sekota": 59,
    "Axum": 66,
    "Shire": 67,
    "Humera": 65,
    "Kartum": 81,
}
    start = "Addis Ababa"
    goal = "Moyale"
    result = informedSearch(graph).ucs(start, goal, [])
    print(result)
    
    
    