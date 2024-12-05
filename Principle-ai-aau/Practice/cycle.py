#!/usr/bin/python3
""" Detect cycle in a graph """

# Define the graph
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
in_path = {node: False for node in graph.keys()}

# Variables to store the number of cycles and the list of all cycles
cycles_detected = 0
all_cycles = []

def dfs(node, current_path):
    """
    Perform DFS to detect cycles in the graph.

    :param node: Current node being visited
    :param current_path: Path taken to reach the current node
    """
    global cycles_detected

    # Check if the node is already in the current path (cycle detected)
    if in_path[node]:
        cycles_detected += 1
        cycle_start_index = current_path.index(node)
        detected_cycle = current_path[cycle_start_index:] + [node]
        
        # Avoid adding duplicate cycles and permutations of cycles
        if sorted(detected_cycle) not in [sorted(cycle) for cycle in all_cycles]:
            all_cycles.append(detected_cycle)
            print(f"Cycle detected: {detected_cycle}")
        return

    # Mark the node as visited and part of the current path
    visited[node] = True
    in_path[node] = True
    current_path.append(node)

    # Explore neighbors
    for neighbor in graph[node]:
        dfs(neighbor, current_path)

    # Backtrack: remove the node from the current path and mark it as not in path
    in_path[node] = False
    current_path.pop()

if __name__ == "__main__":
    # Start DFS from each node in the graph
    for head in graph.keys():
        if not in_path[head]:
            dfs(head, [])

    print(f"Total cycles detected: {cycles_detected}")
    print(f"All cycles: {all_cycles}")
