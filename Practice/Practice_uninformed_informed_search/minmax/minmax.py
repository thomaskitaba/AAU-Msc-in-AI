#!/usr/bin/python3
class minimax_Coffee:
    def __init__(self, graph, utilities):
        """
        Initialize the search problem.
        :param graph: Dictionary representing the connections between locations (graph).
        :param utilities: Dictionary of utility values for terminal nodes.
        :param initial_state: The starting state of the agent.
        """
        self.graph = graph
        self.utilities = utilities
        
    def minimax(self, current_node, is_maximizer, alpha, beta):
        if is_maximizer:
            max_utility = float('-inf')
            # return utility if we reached the end of the node
            if current_node not in graph or not graph.get(current_node):
                return self.utilities.get(current_node, 0)
            for neighbor in graph.get(current_node, []):
                value = self.minimax(neighbor, False, alpha, beta)
                max_utility = max(value, max_utility)
                alpha = max(max_utility, value)
                if alpha >= beta:
                    break
                
            return max_utility
        
        if not is_maximizer: 
            min_utility = float("inf")
            if current_node not in graph or not graph.get(current_node):
                return self.utilities.get(current_node)
            
            for neighbor in graph.get(current_node, []):
                value = self.minimax(neighbor, True, alpha, beta)
                min_utility = min(value, min_utility)
                # pruning 
                beta = min(min_utility, value)
                if beta <= alpha:
                    break
            return min_utility
# # Example Usage
if __name__ == "__main__":
    # Graph of Ethiopia's cities
    graph = {
    "Addis Ababa": ["Ambo", "Adama", "Buta Jirra"],
    "Ambo": ["Gedo", "Nekemte"],
    "Adama": ["Bredawe", "Mojo"],
    "Buta Jirra": ["Woliso", "Worabe"],
    "Woliso": [],  # Add Woliso as a terminal node
    "Gedo": ["Shambu", "Fincha"],
    "Bredawe": ["Harar", "Chiro"],
    "Mojo": ["Dilla"],
    "Worabe": ["Hossana", "Durame"],
    "Durame": ["Bench Naji"],
    "Bench Naji": ["Tepi"],
    "Dilla": ["Kaffa"],
    "Nekemte": [],
    }

    utilities = {
        "Shambu": 4,
        "Fincha": 5,
        "Gimbi": 8,
        "Harar": 10,
        "Chiro": 6,
        "Dilla": 9,
        "Tepi": 6,
        "Kaffa": 7,
        "Hossana": 6,
        "Durame": 5,
        "Bench Naji": 5,
        "Nekemte": 8,
        "Woliso": 0,  # Assign utility for Woliso
    }
    
    # Starting state
    root = "Addis Ababa"

    # Create the search problem instance
    problem = minimax_Coffee(graph, utilities)

    # Run MiniMax algorithm
    # best_utility, path = problem.minimax(root, True)
    best_utility= problem.minimax(root, True, float("-inf"), float("inf"))
    print(best_utility)
    # print(path)
  