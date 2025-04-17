#!/usr/bin/python3
def has_cycle(graph):
    def dfs(node):
        # Add the current node to the recursion stack
        rec_stack.add(node)
        visited.add(node)

        # Explore all neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Cycle detected
        # Remove the current node from the recursion stack
        rec_stack.remove(node)
        return False

    visited = set()
    rec_stack = set()

    # Check for cycles in all components of the graph
    for node in graph:
        if node not in visited:
            print(f"node: {node}")
            if dfs(node):
                return True
    return False

# Sample graphs
if __name__ == "__main__":
    # Graph with a cycle
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [3],
        3: [0]  # Back edge forming a cycle
    }

    # Graph without a cycle
    graph_without_cycle = {
        0: [1],
        1: [2],
        2: [3],
        3: []  # No back edge
    }

    # Empty graph
    empty_graph = {}

    # Disconnected graph
    disconnected_graph = {
        0: [1],
        1: [],
        2: [3],
        3: []
    }
    graph = {
    "Addis Ababa": ["Adama", "Bahir Dar"],
    "Adama": ["Hawassa"],
    "Bahir Dar": ["Gondar", "Mekele"],
    "Hawassa": [],
    "Gondar": ["Mekele"],
    "Mekele": ["Addis Ababa", "Gonder"]
}
    print("Graph with cycle:", has_cycle(graph_with_cycle))  # Output: True
    print("Graph without cycle:", has_cycle(graph_without_cycle))  # Output: False
    print("Empty graph:", has_cycle(empty_graph))  # Output: False
    print("Disconnected graph:", has_cycle(disconnected_graph))  # Output: False
    print("=================")
   
    